# Prueba técnica: Data pipeline

**Descripción:**
Desarrollar un pipeline de análisis de datos utilizando los datos abiertos de la Ciudad de México
correspondientes a las ubicaciones de las unidades del metrobús para que pueda ser
consultado mediante un API Rest filtrando por unidad o por alcaldía.

**Requerimientos y reglas de negocio**

  * Presentar un diagrama con el diseño de su solución
  * Generar un modelo de datos y su DDL
  * Obtener la alcaldía correspondiente a cada posición, el candidato tendrá la libertad de elegir el método que consideré más adecuado.
  * Almacenar la información en una base de datos
  * Diseñar e implementar un API que permita consultar la información almacenada, con las siguientes características:
    * Obtener una lista de unidades disponibles
    * Consultar la ubicación de una unidad dado su ID
    * Obtener una lista de alcaldías disponibles
    * Obtener la lista de unidades que se encuentren dentro de una alcaldía
    
**Código**
  * El candidato tendrá completa libertad de elegir el stack tecnológico
  * Incluir comentarios en el código
  * Manejar control de versiones
  * Utilizar docker para empaquetar su(s) servicio(s)

**Puntos extra**
  * Implementar el API usando GraphQL
  * Las configuraciones necesarias para desplegar su(s) servicio(s) en kubernetes
  * Implementar su solución usando programación funcional
  * Incluir pruebas unitarias
  
## Diagrama de solucion

  ![image](https://user-images.githubusercontent.com/61101012/173300968-9e3234c5-a445-41a5-8018-ae12bf93bfe0.png)

## DDL

```SQL
CREATE TABLE metrobus (
  id int(11) NOT NULL,
  date_updated datetime DEFAULT NULL,
  vehicle_id int(11) DEFAULT '0',
  vehicle_label int(11) DEFAULT '0',
  vehicle_current_status int(11) DEFAULT '0',
  position_latitude float DEFAULT '0',
  position_longitude float DEFAULT '0',
  geographic_point varchar(100) DEFAULT NULL,
  position_speed int(11) DEFAULT '0',
  position_odometer int(11) DEFAULT '0',
  trip_schedule_relationship int(11) DEFAULT '0',
  trip_id int(11) DEFAULT '0',
  trip_start_date date DEFAULT '9999-12-31',
  trip_route_id int(11) DEFAULT '0',
  alcaldia varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Obtener alcaldias

![image](https://user-images.githubusercontent.com/61101012/173397392-59738ae2-209b-4532-9993-5af3d7b40c88.png)

```JavaScript
var ss = SpreadsheetApp.getActiveSpreadsheet();
var sheet = ss.getActiveSheet();
var dataRangeAll = sheet.getDataRange();
var ultimaFila = dataRangeAll.getLastRow();

// Alcaldias a buscar
var alcaldias = ["Azcapotzalco",
  "Álvaro Obregón",
  "Benito Juárez",
  "Coyoacán",
  "Cuajimalpa",
  "Cuauhtémoc",
  "Gustavo A. Madero",
  "Iztacalco",
  "Iztapalapa",
  "La Magdalena Contreras",
  "Miguel Hidalgo",
  "Milpa Alta",
  "Tlalpan",
  "Tláhuac",
  "Venustiano Carranza",
  "Xochimilco"]

// Agregar apps Script a hoja de calculo
function onOpen() {  
  var ui = SpreadsheetApp.getUi();
  // Nombre del apps Scrip
  ui.createMenu('Geocodificación')
  // Nombre de la funcion, método de inicialización
    .addItem('Convertir coordenadas en direcciones', 'geocodificacion_inversa')
    .addToUi();
}

// Busca alcaldia
function getAlcaldia(direcciones){
  for(let i of direcciones)
    for(let j of alcaldias)
      if(i.formatted_address.search(j) >= 0)
        return j
      
  return direccion
}

// Método de inicialización
function geocodificacion_inversa() {
  // Espesificar rangos de lectura en la hoja de calculo
  var filaInicial = 2;
  var dataRange = sheet.getRange(filaInicial, 1,ultimaFila, 3);
  var data = dataRange.getValues();

  // Consultar politicas de uso de la api 
  for(let i = 0; i <= (i + 100) ; i++) {
    var fila = data[i];

    var latitud = fila[0];
    var longitud = fila[1];

    if(latitud != "" && longitud != "") {
      var reverseGeocoder = Maps.newGeocoder().reverseGeocode(latitud, longitud);
      var resultado = reverseGeocoder.results;

      if(resultado) 
        sheet.getRange(filaInicial + i, 3).setValue(getAlcaldia(resultado));
      
    }
  }
}
```

**Método implementado:**
https://developers.google.com/apps-script/reference/maps/geocoder#reversegeocodelatitude,-longitude

## Almacenar la información

Importar .csv separado por comas: https://docs.google.com/spreadsheets/d/17Phwm7Z9QjFnEsYLKi1z0lQuhqSQ49GVijaq8fiKU3M/edit?usp=sharing

## API

![image](https://user-images.githubusercontent.com/61101012/173432778-3ffa0684-794a-4899-a985-be8fd2380b62.png)

## Docker

```
docker push oalmanzao/image_demo:tagname
```
