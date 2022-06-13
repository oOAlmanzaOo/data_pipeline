# Funciones externas
from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

# Funciones locales
from models import Base, MetroBus
from config import engine, SessionLocal
from schemas import Metro, MetroGeoPosicion, MetroAlcaldia

# Inicializar modelos
Base.metadata.create_all(bind=engine)

# Inicializar rutas
metroBus = APIRouter()


def get_db():
    # Obtener estado de la conexion
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@metroBus.get("/")
# Redirecciona a la documentacion de la api
def index():
    response = RedirectResponse(url='/docs')
    return response


@metroBus.get("/getUnidadesActivas", response_model=List[Metro])
# Obtener una lista de unidades disponibles
# vehicle_current_status: 1 (disponible) y 2 (no disponible)
#
# Metodo: GET
# Headers: None
# Req: None
# Response:
#   [
#       {
#           "id": int,
#           "date_updated": "YYYY-MM-DDTHH:mm:SS",
#           "vehicle_id": int,
#           "vehicle_label": int,
#           "vehicle_current_status": int,
#           "position_latitude": int,
#           "position_longitude": int,
#           "geographic_point": "string",
#           "position_speed": int,
#           "position_odometer": int,
#           "trip_schedule_relationship": int,
#           "trip_id": int,
#           "trip_start_date": "YYYY-MM-DD",
#           "trip_route_id": int,
#           "alcaldia": "string"
#       }
#   ]
def getUnidadesActivas(db: Session = Depends(get_db)):
    return db.query(MetroBus).filter(MetroBus.vehicle_current_status == 1).all()


@metroBus.get("/getGeoposicion/{id}", response_model=MetroGeoPosicion)
# Consultar la ubicación de una unidad dado su ID
#
# Metodo: GET
# Headers: None
# Req: id: init
# Response:
#   {
#       "id": int,
#       "date_updated": "YYYY-MM-DDTHH:mm:SS",
#       "vehicle_id": int,
#       "vehicle_label": int,
#       "vehicle_current_status": int,
#       "position_latitude": int,
#       "position_longitude": int,
#       "geographic_point": "string",
#       "position_speed": int,
#       "position_odometer": int,
#       "trip_schedule_relationship": int,
#       "trip_id": int,
#       "trip_start_date": "YYYY-MM-DD",
#       "trip_route_id": int,
#       "alcaldia": "string"
#   }
def getGeoposicion(id: int, db: Session = Depends(get_db)):
    return db.query(MetroBus).filter(MetroBus.id == id).first()


@metroBus.get("/getAlcaldias", response_model=List[MetroAlcaldia])
# Obtener una lista de unidades disponibles
#
# Metodo: GET
# Headers: None
# Req: None
# Response:
#   [
#       {
#           "alcaldia": "string"
#       }
#   ]
def getAlcaldias(db: Session = Depends(get_db)):
    return db.query(MetroBus.alcaldia).filter(MetroBus.alcaldia != "").group_by(MetroBus.alcaldia).all()


@metroBus.get("/getUnidadesFAlcaldia", response_model=List[Metro])
# Obtener la lista de unidades que se encuentren dentro de una alcaldía
#
# Metodo: GET
# Headers: None
# Req: alcaldia: string
# Response:
#   [
#       {
#           "id": int,
#           "date_updated": "YYYY-MM-DDTHH:mm:SS",
#           "vehicle_id": int,
#           "vehicle_label": int,
#           "vehicle_current_status": int,
#           "position_latitude": int,
#           "position_longitude": int,
#           "geographic_point": "string",
#           "position_speed": int,
#           "position_odometer": int,
#           "trip_schedule_relationship": int,
#           "trip_id": int,
#           "trip_start_date": "YYYY-MM-DD",
#           "trip_route_id": int,
#           "alcaldia": "string"
#       }
#   ]
def getUnidadesFAlcaldia(alcaldia: str, db: Session = Depends(get_db)):
    return db.query(MetroBus).filter(MetroBus.alcaldia == alcaldia).all()
