FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all necessary files
COPY main.py .
COPY app.py .
COPY init_db.py .
COPY .env .

# Expose Streamlit port
EXPOSE 8501

# Use Streamlit as the main command instead of main.py
CMD ["streamlit", "run", "app.py"]

# -----------------------------
# Build Command:
# -----------------------------
# docker build -t rahulagowda04/smarthealth-assistant .
#
# Run Command:
# -----------------------------
# For Windows PowerShell:
# docker run -p 8501:8501 rahulagowda04/smarthealth-assistant
#
# Or with environment variables (if not using .env file):
# docker run -p 8501:8501 -e NEO4J_URI="your_neo4j_uri" -e NEO4J_USERNAME="your_username" -e NEO4J_PASSWORD="your_password" -e GOOGLE_API_KEY="your_api_key" rahulagowda04/smarthealth-assistant