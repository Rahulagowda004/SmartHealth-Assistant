# 🤖 SmartHealth Assistant

A Streamlit medical chatbot powered by Google Gemini and Neo4j that remembers your medical history, tracks symptoms and vitals over time, and provides personalized health advice based on your past data. 🏥💡

## 📸 Application Screenshots

### Main Chat Interface

![SmartHealth Assistant Interface](screenshots/chat-interface.png)

The main interface features:

- **User Information Panel**: Configure your username and API settings
- **API Configuration**: Secure Google API key management with visibility toggle
- **Interactive Chat**: Natural conversation flow with the AI assistant
- **About Section**: Clear description of the assistant's capabilities

### Sample Conversation Flow

![Medical Conversation Example](screenshots/medical-conversation.png)

The assistant can:

- Recall previous medical visits and recorded symptoms
- Provide detailed health analysis based on historical data
- Recommend immediate medical attention when necessary
- Maintain context across conversations

### Neo4j Database Visualization

![Database Graph Structure](screenshots/neo4j-database.png)

The graph database structure shows:

- **Nodes**: Patient, Date, Symptoms, and Vitals entities
- **Relationships**: HAS_SYMPTOMS, HAS_VITALS, and ON_THE_DAY connections
- **Properties**: Comprehensive health data including vital signs and symptom descriptions

### Database Schema Overview

![Database Information Panel](screenshots/database-schema.png)

Key database components:

- **4 Node Types**: Patient, Date, Symptoms, Vitals
- **3 Relationship Types**: Connecting health data across time
- **Rich Properties**: Blood pressure, heart rate, temperature, respiratory rate, and more

## 🛠️ Technology Stack

- **Streamlit** 🎨: Modern web-based frontend for user interaction
- **Google Gemini 1.5** 🤖: Advanced Large Language Model for natural language processing
- **Neo4j Database** 🗃️: Graph database for storing interconnected patient health records
- **LangChain Framework** 🧩: Orchestrating conversation flow and LLM interactions
- **Docker** 🐳: Containerization of the application

## 🌟 Core Features

### Patient Data Management 📋

- Stores patient symptoms and vitals in Neo4j graph database 🗄️
- Creates daily records with timestamps 📅
- Maintains relationships between patients, dates, symptoms, and vitals 🔗
- Retrieves previous patient data for historical analysis 🔍

### Natural Language Processing 🗣️

- Extracts medical symptoms and vitals from conversation 💬
- Validates medical information before storage ✅
- Maintains conversation context using patient history 📖
- Provides health insights based on current and previous information 🏥

### Graph Data Structure 🧩

```
(Patient)-[:ON_THE_DAY]->(Date)
(Date)-[:HAS_SYMPTOMS]->(Symptoms)
(Date)-[:HAS_VITALS]->(Vitals)
```

**Tracked Health Metrics:**

- Blood pressure, heart rate, respiratory rate, temperature
- Symptoms: fatigue, headache, shortness of breath, chest pain, dizziness
- Patient demographics and medical history

## 🔑 Key Components

- **Neo4jConnector** 🔌: Handles database connections and queries
- **PatientGraphManager** 📊: Manages patient data operations
- **MedicalInfo** 🏷️: Pydantic model for parsing medical information
- **MedicalApp** 🏗️: Main application logic with LangChain workflow
- **StreamlitApp** 🎨: Web-based frontend for user interaction

## 📋 Requirements

- Python 3.11+ 🐍
- Neo4j Database 🗄️
- Google API Key for Gemini model 🔑
- Required Python packages in requirements.txt 📜

## 🔧 Environment Variables

```bash
NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=your_username
NEO4J_PASSWORD=your_password
GOOGLE_API_KEY=your_google_api_key
```

## 🏗️ Setup Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/smarthealth-assistant.git
cd smarthealth-assistant
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start Neo4j and configure it using the provided environment variables.

5. Run the Streamlit application:

```bash
streamlit run app.py
```

## 🐳 Docker Support

### Build and Run Instructions

1. Build the Docker image:

```bash
docker build -t smarthealth-assistant .
```

2. Run the container:

```bash
docker run -it -e NEO4J_URI="" -e NEO4J_USERNAME="" -e NEO4J_PASSWORD="" -e GOOGLE_API_KEY="" smarthealth-assistant
```

Ensure you have a valid .env file with the required environment variables before running the container.

## 🚀 Usage

1. **Configure User Information**: Set your username in the sidebar
2. **Add API Key**: Enter your Google API key in the API Configuration section
3. **Start Chatting**: Interact with the SmartHealth Assistant about your health
4. **Track Health Data**: The system automatically stores symptoms and vitals
5. **Review History**: Access your previous health records and trends
6. **Get Insights**: Receive personalized health advice based on your data

## 🔍 Example Use Cases

- **Symptom Tracking**: "I have a headache and feel dizzy"
- **Vital Signs Recording**: "My blood pressure is 130/85 and heart rate is 92"
- **Historical Analysis**: "What were my symptoms on June 11th, 2025?"
- **Health Monitoring**: Track patterns and changes in your health over time

## 📊 Database Visualization

The Neo4j database can be explored using the built-in browser interface, showing the interconnected nature of your health data across time. Each patient visit creates new nodes and relationships, building a comprehensive health timeline.

## 📜 License

This project is licensed under the MIT License. 📄

---

**⚠️ Important Disclaimer**: This is an AI assistant for informational purposes only. Always consult with healthcare professionals for medical advice and diagnosis.
