# Python resmi imajını temel al
FROM python:3.10-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Çalışma portunu belirt (genelde 8080 Fly.io için önerilir)
ENV PORT 8080

# Flask uygulamasını çalıştır
CMD ["python", "app.py"]
