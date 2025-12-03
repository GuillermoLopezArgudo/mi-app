FROM python:3.12-alpine

# Paquetes necesarios para compilar cryptography y dependencias básicas
RUN apk add --no-cache \
    build-base \
    openssl-dev \
    libffi-dev \
    mariadb-connector-c-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
