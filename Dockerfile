# Imagen oficial Python 3.7
FROM python:3.7

# Work Directory
WORKDIR /app

# Copiar codigo del proyecto en el work directory
COPY requirements.txt ./

# Actualizar pip
RUN pip install --upgrade pip

# Instalar dependencias del proyecto
RUN pip --no-cache-dir install -r requirements.txt

# Copiar codigo del proyecto en el work directory
COPY . /app

# Correr la aplicacion
CMD ["python", "api/app.py", "pro"]