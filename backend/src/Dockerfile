# backend/Dockerfile

FROM python:3.10.1-slim

WORKDIR /src

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]

