# Base ligera de Python para ejecutar FastAPI.
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor.
WORKDIR /app

# Flags de runtime recomendados para contenedores.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependencias de backend.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia backend y frontend estático servidos por FastAPI.
COPY app ./app
COPY *.html ./
COPY *.css ./
COPY *.js ./
COPY assets ./assets

# Puerto interno expuesto por Uvicorn.
EXPOSE 8000

# Comando de inicio del servidor API.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
