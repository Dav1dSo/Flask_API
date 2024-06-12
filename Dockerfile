FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .env . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]