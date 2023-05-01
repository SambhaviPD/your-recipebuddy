# backend/Dockerfile

FROM python:3.10.1-slim

WORKDIR /app

RUN apt-get update

# Copy requirements.txt file
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8080:8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
