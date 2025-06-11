FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY init_db.py .

CMD ["python", "main.py"]

# -----------------------------
# docker build -t rahulagowda04/personal_medical_assistant .
#
# Run Command:
# -----------------------------
# For Windows PowerShell:
#docker run -it -e NEO4J_URI="" -e NEO4J_USERNAME="" -e NEO4J_PASSWORD="" -e GOOGLE_API_KEY="" rahulagowda04/personal_medical_assistant

docker run -it -e NEO4J_URI="neo4j+s://065f4ada.databases.neo4j.io" -e NEO4J_USERNAME="neo4j" -e NEO4J_PASSWORD="aYYluK7n_mVFoF7l0DUW1LXKZpUAqG5cy_GfS9t32Ro" -e GOOGLE_API_KEY="AIzaSyB8-veRiwdkBR-EYUPRziD1n8TvqAnDpLc" rahulagowda04/personal_medical_assistant