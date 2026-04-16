FROM python:3.12-slim

WORKDIR /app

# Ensure logs don't buffer in Cloud Run
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files into /app
COPY . .

# Run Uvicorn mapping to the $PORT assigned by Cloud Run
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
