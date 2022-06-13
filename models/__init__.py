from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Float, Date
from config import Base


class MetroBus(Base):
    # Nombre de la tabla
    __tablename__ = "metrobus"

    # Especificacion de columnas
    id = Column(Integer, primary_key=True, autoincrement=False)
    date_updated = Column(DateTime)
    vehicle_id = Column(Integer, default=0)
    vehicle_label = Column(Integer, default=0)
    vehicle_current_status = Column(Integer, default=0)
    position_latitude = Column(Float, default=0)
    position_longitude = Column(Float, default=0)
    geographic_point = Column(String(100))
    position_speed = Column(Integer, default=0)
    position_odometer = Column(Integer, default=0)
    trip_schedule_relationship = Column(Integer, default=0)
    trip_id = Column(Integer, default=0)
    trip_start_date = Column(Date)
    trip_route_id = Column(Integer, default=0)
    alcaldia = Column(String(100))
