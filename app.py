import streamlit as st
from main import MedicalApp, Neo4jConnector
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

with st.sidebar:
    st.subheader("User Information")
    username = st.text_input("Your Username", key="username").lower()

st.title("🏥 SmartHealth Assistant")
st.caption("🚀 A Streamlit medical chatbot powered by Google Gemini and Neo4j")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I'm your SmartHealth Assistant. How can I help you with your health today?"}]

if "app_instance" not in st.session_state:
    st.session_state["app_instance"] = None

if "workflow_app" not in st.session_state:
    st.session_state["workflow_app"] = None

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    # Get credentials from environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_username = os.getenv("NEO4J_USERNAME")
    neo4j_password = os.getenv("NEO4J_PASSWORD")
    
    if not google_api_key:
        st.error("Google API Key not found in .env file")
        st.stop()
    
    if not all([neo4j_uri, neo4j_username, neo4j_password]):
        st.error("Neo4j credentials not found in .env file")
        st.stop()
    
    if not username:
        st.info("Please enter your username.")
        st.stop()

    # Initialize the medical app if not already done
    if st.session_state["app_instance"] is None:
        try:
            connector = Neo4jConnector(neo4j_uri, neo4j_username, neo4j_password)
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=google_api_key)
            st.session_state["app_instance"] = MedicalApp(neo4j_connector=connector, llm_model=llm, username=username)
            st.session_state["workflow_app"] = st.session_state["app_instance"].setup_workflow(username)
        except Exception as e:
            st.error(f"Failed to connect to database: {str(e)}")
            st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    try:
        # Extract medical data and store in Neo4j
        input_messages = [HumanMessage(prompt)]
        st.session_state["app_instance"].cypher_generator(prompt)
        
        # Get response from the workflow
        config = {"configurable": {"thread_id": username}}
        response = st.session_state["workflow_app"].invoke({"messages": input_messages}, config)["messages"][-1]
        msg = response.content
        
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")