"""Servidor principal FastAPI para el proyecto Taller Web.

Este archivo define las rutas principales, la configuración de archivos estáticos,
las plantillas Jinja2 y los endpoints de API didácticos para la clase.
"""

import os
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Cargar variables de entorno desde el archivo .env si está presente
load_dotenv()

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Taller Web con Python",
    description="Aplicación web didáctica desarrollada paso a paso con FastAPI, Jinja2 y Coolify.",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Directorio base para rutas absolutas seguras
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Montaje de archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Configuración del motor de plantillas Jinja2
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# ==============================================================================
# Rutas de Vistas (HTML con Jinja2)
# ==============================================================================

@app.get("/", response_class=HTMLResponse, summary="Página de Inicio")
async def read_home(request: Request):
    """Renderiza la página de inicio del taller.

    Args:
        request (Request): Objeto de solicitud HTTP de FastAPI.

    Returns:
        HTMLResponse: Plantilla index.html renderizada con contexto didáctico.
    """
    modulos_clase = [
        {
            "id": 1,
            "titulo": "1. Estructura y Primer Deploy",
            "descripcion": "Creación del proyecto base, Dockerfile, configuración en Coolify y healthchecks.",
            "estado": "Completado",
            "icono": "bi-rocket-takeoff"
        },
        {
            "id": 2,
            "titulo": "2. Rutas y Parámetros Dinámicos",
            "descripcion": "Manejo de Path Parameters, Query Parameters y renderizado de plantillas Jinja2.",
            "estado": "En curso",
            "icono": "bi-signpost-split"
        },
        {
            "id": 3,
            "titulo": "3. Formularios y Entrada de Datos",
            "descripcion": "Captura de formularios HTML (POST), validación de datos con Pydantic y respuestas.",
            "estado": "Pendiente",
            "icono": "bi-input-cursor-text"
        },
        {
            "id": 4,
            "titulo": "4. Persistencia y Base de Datos",
            "descripcion": "Conexión a SQLite / PostgreSQL, modelos ORM (SQLAlchemy) y migraciones.",
            "estado": "Pendiente",
            "icono": "bi-database"
        },
        {
            "id": 5,
            "titulo": "5. API REST e Integración Frontend",
            "descripcion": "Consumo asíncrono con JavaScript (fetch) y documentación interactiva OpenAPI/Swagger.",
            "estado": "Pendiente",
            "icono": "bi-cpu"
        },
    ]

    contexto = {
        "request": request,
        "titulo": "Taller Web con Python",
        "descripcion": "Proyecto base para el desarrollo en clase paso a paso",
        "servidor_entorno": os.getenv("ENVIRONMENT", "VPS Coolify / Desarrollo"),
        "fecha_actual": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "modulos": modulos_clase,
    }
    return templates.TemplateResponse(request=request, name="index.html", context=contexto)


@app.get("/about", response_class=HTMLResponse, summary="Página Acerca de")
async def read_about(request: Request):
    """Renderiza la página informativa del taller.

    Args:
        request (Request): Objeto de solicitud HTTP de FastAPI.

    Returns:
        HTMLResponse: Plantilla about.html renderizada.
    """
    contexto = {
        "request": request,
        "titulo": "Acerca del Taller Web",
    }
    return templates.TemplateResponse(request=request, name="about.html", context=contexto)


# ==============================================================================
# Rutas de API y Salud (Healthcheck)
# ==============================================================================

@app.get("/health", summary="Healthcheck para Coolify y Docker")
async def healthcheck():
    """Endpoint de verificación de salud utilizado por Coolify y Traefik.

    Returns:
        dict: Estado actual de la aplicación, timestamp y versión.
    """
    return {
        "status": "healthy",
        "app": "tallerweb",
        "version": "1.1.0",
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/api/info", summary="Información del Servidor")
async def get_info():
    """Endpoint JSON de ejemplo que retorna metadatos del entorno.

    Returns:
        dict: Diccionario con detalles del entorno de ejecución.
    """
    return {
        "framework": "FastAPI",
        "lenguaje": "Python 3.11+",
        "despliegue": "Coolify Container",
        "puerto": os.getenv("PORT", "8000"),
        "docs_url": "/docs",
    }

