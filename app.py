# Funciones externas
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

# Funciones locales
from routes import metroBus

# Inicializar app
app = FastAPI()


@app.get("/")
# Redirecionar a documentacion de la api
def index():
    response = RedirectResponse(url='/docs')
    return response


@app.exception_handler(StarletteHTTPException)
# Excepción url no encontrada
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")

# Incluir rutas
app.include_router(metroBus, prefix="/api", tags=["api"],)
