from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

# Obtiene valores del .env
config = dotenv_values(".env")

# host = 'localhost'
host = config['MYSQL_HOST']

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{user}:{pasw}@{host}:{port}/{db}?charset=utf8".format(
    user=config['MYSQL_USER'],
    pasw=config['MYSQL_ROOT_PASSWORD'],
    host=host,
    port=config['MYSQL_PORT'],
    db=config['MYSQL_DATABASE']
)

print(SQLALCHEMY_DATABASE_URL)

# Conexion a la BD
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear Sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea un Base de la base de datos
Base = declarative_base()
