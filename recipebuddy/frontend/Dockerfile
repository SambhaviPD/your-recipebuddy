# frontend/Dockerfile

FROM python:3.10.1-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501:8501

RUN pip install -e .

CMD streamlit run --server.port 8501 --server.enableCORS false src/recipebuddy_frontend/Recipe_Buddy.py
