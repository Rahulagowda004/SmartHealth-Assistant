FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY init_db.py .

# Run the application
CMD ["python", "main.py"]

# Build Command:
# -----------------------------
# docker build -t rahulagowda04/personal_medical_assistant .
#
# Run Command:
# -----------------------------
# For Windows PowerShell:
#docker run -it -e NEO4J_URI="" -e NEO4J_USERNAME="" -e NEO4J_PASSWORD="" -e GOOGLE_API_KEY="" rahulagowda04/personal_medical_assistant