# 🚀 Taller Web con Python (FastAPI + Coolify)

Proyecto base didáctico para el desarrollo paso a paso de una aplicación web completa en clase utilizando **Python**, **FastAPI**, plantillas **Jinja2**, **Docker** y despliegue continuo en **Coolify**.

---

## 📁 Estructura del Proyecto

`	ext
tallerweb/
├── app/
│   ├── __init__.py           # Inicializador del paquete
│   ├── main.py               # Aplicación FastAPI, rutas y endpoints
│   ├── static/               # Archivos estáticos
│   │   ├── css/styles.css    # Estilos CSS modernos (Dark mode & Bootstrap 5)
│   │   └── js/app.js         # Lógica interactiva en cliente (fetch API)
│   └── templates/            # Plantillas HTML con Jinja2
│       ├── base.html         # Plantilla maestra con navbar y footer
│       ├── index.html        # Vista principal con plan de clase
│       └── about.html        # Vista informativa sobre el taller
├── .dockerignore             # Exclusiones para la imagen Docker
├── .env.example              # Variables de entorno de ejemplo
├── .gitignore                # Archivos ignorados por Git
├── docker-compose.yml        # Orquestación para ejecución local o servidor
├── Dockerfile                # Configuración de contenedor optimizada
├── README.md                 # Guía didáctica y de despliegue
└── requirements.txt          # Dependencias de Python
`

---

## 🛠️ Ejecución Local

### Opción 1: Con Python (Entorno Virtual)

1. Crear y activar un entorno virtual:
   `ash
   # En Windows:
   python -m venv venv
   .\venv\Scripts\activate

   # En Linux/macOS:
   python3 -m venv venv
   source venv/bin/activate
   `

2. Instalar dependencias:
   `ash
   pip install -r requirements.txt
   `

3. Iniciar el servidor en modo desarrollo con recarga automática:
   `ash
   uvicorn app.main:app --reload --port 8000
   `

4. Abrir en el navegador:
   - Sitio Web: [http://localhost:8000](http://localhost:8000)
   - Documentación Interactiva (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)
   - Healthcheck: [http://localhost:8000/health](http://localhost:8000/health)

---

### Opción 2: Con Docker Compose

`ash
docker compose up --build
`

La aplicación quedará disponible inmediatamente en [http://localhost:8000](http://localhost:8000).

---

## 🌐 Despliegue en VPS con Coolify

Para montar este proyecto en tu VPS de pruebas con **Coolify**, sigue estos sencillos pasos:

1. **Entra a tu panel de Coolify**:
   - Ve al proyecto o entorno donde quieras alojarlo (ej: *Testing* o *Default*).
2. **Crear Nuevo Recurso**:
   - Haz clic en **+ New Resource** → **Public Repository** (o Private via GitHub App).
   - Ingresa la URL del repositorio: https://github.com/ofazzito/tallerweb
   - Rama (*Branch*): main
3. **Configuración de la Aplicación**:
   - **Build Pack**: Selecciona **Dockerfile** (Coolify detectará automáticamente el archivo Dockerfile en la raíz).
   - **Port**: 8000 (puerto expuesto).
   - **Health Check Path**: /health
4. **Dominio / Subdominio**:
   - Asigna un dominio o deja que Coolify genere uno automático (ej. 	allerweb.tudominio.com).
5. **Deploy**:
   - Haz clic en **Deploy**. Coolify construirá la imagen Docker, configurará el proxy Traefik y publicará la web con SSL automáticamente.

---

## 🗺️ Endpoints y Rutas Disponibles

| Método | Ruta | Descripción |
|---|---|---|
| GET | / | Página de bienvenida con la ruta didáctica de la clase |
| GET | /about | Información del taller y conceptos a aprender |
| GET | /health | Healthcheck para Docker y Traefik (retorna 200 OK) |
| GET | /api/info | Endpoint JSON con metadatos del servidor |
| GET | /docs | Interfaz interactiva OpenAPI / Swagger |
| GET | /redoc | Documentación alternativa ReDoc |

---

## 👨‍🏫 Desarrollo Paso a Paso en Clase

1. **Paso 1 (Actual)**: Servidor base en FastAPI, Jinja2, Dockerfile y despliegue continuo.
2. **Paso 2**: Parámetros de ruta (/saludo/{nombre}), consultas (?categoria=python) y renderizado dinámico.
3. **Paso 3**: Formularios HTML con Form(...) y validación de esquemas con Pydantic.
4. **Paso 4**: Base de datos SQLite / PostgreSQL con SQLAlchemy para persistencia real.
5. **Paso 5**: Consumo asíncrono con JavaScript mediante etch() para componentes reactivos.
