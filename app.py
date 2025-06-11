"""
SmartHealth Assistant - A Medical Chatbot Application

This Streamlit-based medical assistant application provides personalized health support 
by combining Google Gemini AI with Neo4j graph database for persistent health data storage.

Key Features:
- Interactive chat interface for health consultations
- Automatic extraction and storage of medical symptoms and vitals
- Historical health data tracking and context-aware responses
- User-specific health profiles with temporal data organization
- Secure credential management via environment variables

Architecture:
- Frontend: Streamlit web interface with chat functionality
- AI Engine: Google Gemini (gemini-1.5-flash) for natural language processing
- Database: Neo4j graph database for structured health data storage
- Workflow: LangGraph for conversation state management and memory

Data Flow:
1. User enters health information through chat interface
2. AI extracts symptoms and vitals from natural language input
3. Data is stored in Neo4j with user-specific nodes and date relationships
4. Historical context is retrieved for personalized responses
5. AI provides health advice based on current input and past data
"""

import streamlit as st
from main import MedicalApp, Neo4jConnector
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Sidebar for user information
with st.sidebar:
    st.subheader("User Information")
    username = st.text_input("Your Username", key="username").lower()
    
    # API Key input
    st.markdown("---")
    st.subheader("🔑 API Configuration")
    google_api_key = st.text_input("Google API Key", type="password", key="google_api_key", help="Enter your Google Gemini API key")
    
    # Application description in sidebar
    st.markdown("---")
    st.subheader("🏥 About SmartHealth Assistant")
    st.info("💡 **What I do:** I'm your personal health assistant that remembers your medical history, tracks symptoms and vitals over time, and provides personalized health advice based on your past data.")
    
    # Expandable section for more details
    with st.expander("🔍 Learn More"):
        st.markdown("""
        **🎯 Key Features:**
        - 💬 Natural health conversations
        - 📊 Auto-extract symptoms & vitals
        - 📈 Historical health tracking
        - 🧠 Context-aware responses
        - 🔒 Secure health profiles
        
        **🏗️ How It Works:**
        1. Share health information via chat
        2. I extract & store medical data
        3. Build comprehensive health timeline
        4. Provide personalized advice
        """)

# Main application header
st.title("🏥 SmartHealth Assistant")
st.caption("🚀 A Streamlit medical chatbot powered by Google Gemini and Neo4j")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I'm your SmartHealth Assistant. How can I help you with your health today?"}]

# Initialize session state for application instances
if "app_instance" not in st.session_state:
    st.session_state["app_instance"] = None

if "workflow_app" not in st.session_state:
    st.session_state["workflow_app"] = None

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Main chat input and processing logic
if prompt := st.chat_input():
    # Get Neo4j credentials from environment variables (keep these secure)
    neo4j_uri = os.getenv("NEO4J_URI")
    neo4j_username = os.getenv("NEO4J_USERNAME")
    neo4j_password = os.getenv("NEO4J_PASSWORD")
    
    # Validate required credentials
    if not google_api_key:
        st.error("Please enter your Google API Key in the sidebar")
        st.stop()
    
    if not all([neo4j_uri, neo4j_username, neo4j_password]):
        st.error("Neo4j credentials not found in .env file")
        st.stop()
    
    if not username:
        st.info("Please enter your username.")
        st.stop()

    # Initialize the medical app instance (lazy loading for performance)
    if st.session_state["app_instance"] is None:
        try:
            # Create database connector and AI model instances
            connector = Neo4jConnector(neo4j_uri, neo4j_username, neo4j_password)
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=google_api_key)
            
            # Initialize medical app with user-specific configuration
            st.session_state["app_instance"] = MedicalApp(neo4j_connector=connector, llm_model=llm, username=username)
            st.session_state["workflow_app"] = st.session_state["app_instance"].setup_workflow(username)
        except Exception as e:
            st.error(f"Failed to connect to database or initialize AI model: {str(e)}")
            st.stop()

    # Process user input and generate response
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    try:
        # Extract medical data from user input and store in Neo4j
        input_messages = [HumanMessage(prompt)]
        st.session_state["app_instance"].cypher_generator(prompt)
        
        # Generate AI response using workflow with conversation context
        config = {"configurable": {"thread_id": username}}
        response = st.session_state["workflow_app"].invoke({"messages": input_messages}, config)["messages"][-1]
        msg = response.content
        
        # Update conversation history and display response
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")