FROM python:3.11-slim

# Configuraciones de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# Instalar utilidades mínimas (curl para healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer puerto 8000 para Coolify y Traefik
EXPOSE 8000

# Healthcheck para monitoreo en Coolify
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Ejecución del servidor ASGI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
