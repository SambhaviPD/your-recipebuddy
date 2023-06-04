# backend/Dockerfile

FROM python:3.10.1-slim

WORKDIR /app

RUN apt-get update

# Copy requirements.txt file
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN pip install -e .

EXPOSE 8080:8080

CMD ["uvicorn", "src.recipebuddy_backend.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]