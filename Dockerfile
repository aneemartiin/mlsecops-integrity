# Imagen base de Python
FROM python:3.12-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY check_integrity.py .
COPY model.pkl .
COPY model_hash.txt .
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto: verificar el modelo
CMD ["python", "check_integrity.py"]
