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