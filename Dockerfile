FROM python:3.11-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto (lo puedes cambiar desde docker-compose)
CMD ["python", "send.py"]
