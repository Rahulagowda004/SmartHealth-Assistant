# 🤖 Personal Medical Assistant

A medical assistant chatbot that records and analyzes patient health information using LangChain, Neo4j, Google's Gemini model, and Streamlit for the frontend. 🏥💡

## 🛠️ Technology Stack

- **LangChain Framework** 🧩: Used for orchestrating the conversation flow and LLM interactions
- **Neo4j Database** 🗃️: Graph database for storing patient health records
- **Google Gemini 1.5** 🤖: Large Language Model for natural language processing
- **Streamlit** 🎨: Web-based frontend for user interaction
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
- Diagnoses patients based on current and previous health information 🏥

### Graph Data Structure 🧩

```
(Patient)-[:ON_THE_DAY]->(Date)
(Date)-[:HAS_SYMPTOMS]->(Symptoms)
(Date)-[:HAS_VITALS]->(Vitals)
```

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
git clone https://github.com/yourusername/personal-medical-assistant.git
cd personal-medical-assistant
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

5. Run the backend application:

```bash
python app.py
```

6. Run the Streamlit frontend:

```bash
streamlit run frontend.py
```

## 🐳 Docker Support

### Build and Run Instructions

1. Build the Docker image:

```bash
docker build -t rahulagowda04/personal_medical_assistant .
```

2. Run the container:

```bash
docker run -it -e NEO4J_URI="" -e NEO4J_USERNAME="" -e NEO4J_PASSWORD="" -e GOOGLE_API_KEY="" rahulagowda04/personal_medical_assistant
```

Ensure you have a valid .env file with the required environment variables before running the container.

## 🚀 Usage

1. Start the application ▶️
2. Interact with the chatbot to record patient health data 🏥
3. Query patient records and analyze health trends using Neo4j 📊
4. Retrieve previous patient data and diagnose based on current information 🔍
5. Access the Streamlit frontend for an interactive user experience 🎨

## 📜 License

This project is licensed under the MIT License. 📄
