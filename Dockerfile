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
# docker run -p 8501:8501 -e NEO4J_URI="neo4j+s://065f4ada.databases.neo4j.io" -e NEO4J_USERNAME="neo4j" -e NEO4J_PASSWORD="aYYluK7n_mVFoF7l0DUW1LXKZpUAqG5cy_GfS9t32Ro" -e GOOGLE_API_KEY="AIzaSyB8-veRiwdkBR-EYUPRziD1n8TvqAnDpLc" rahulagowda04/smarthealth-assistant