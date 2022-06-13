# Funciones externas
from datetime import date, datetime
from pydantic import BaseModel


class Metro(BaseModel):
    id: int
    date_updated: datetime = 'YYYY-MM-DDTHH:mm:SS'
    vehicle_id: int
    vehicle_label: int
    vehicle_current_status: int
    position_latitude: float
    position_longitude: float
    geographic_point: str
    position_speed: int
    position_odometer: int
    trip_schedule_relationship: int
    trip_id: int
    trip_start_date: date = 'YYYY-MM-DD'
    trip_route_id: int
    alcaldia: str

    class Config:
        orm_mode = True


class MetroGeoPosicion(BaseModel):
    id: int
    position_latitude: float
    position_longitude: float
    geographic_point: str

    class Config:
        orm_mode = True


class MetroAlcaldia(BaseModel):
    alcaldia: str

    class Config:
        orm_mode = True
