# backend/Dockerfile

FROM python:3.10.1-slim

WORKDIR /app

RUN apt-get update

# Copy requirements.txt file
COPY ./recipebuddy/backend/requirements.txt .
RUN pip install -r requirements.txt

COPY ./recipebuddy/backend/ /app/recipebuddy/backend

EXPOSE 8080

CMD ["python", "recipebuddy/backend/main.py"]