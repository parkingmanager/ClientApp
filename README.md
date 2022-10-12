Este proyecto se integra a través de 4 repositorios:

[DataBase](https://github.com/parkingmanager/RestAPI)
[RestAPI(https://github.com/parkingmanager/RestAPI)
[Utils](https://github.com/parkingmanager/Utils)
[ClientApp](https://github.com/parkingmanager/ClientApp)

# ClientApp
Aplicación Python de escritorio del proyecto Parking Manager

# Aplicación Cliente

El código fuente descrito en este repositorio está desarrollado en Python y permite realizar la digitalización, procesamiento y análisis para construir el bloque de información que será tramitado a través del API REST.
<p align="center">
 <img src="https://user-images.githubusercontent.com/82679673/195241927-977681a5-ffcf-4b75-8109-a04575332359.jpg" width=500><br><sub>
 </p>

## Tabla de contenido

- [Descripción](#descripción).
- [Herramientas de Implementación](#herramientas-de-implementación).
- [Instalación](#instalación).

### Descripción 
 El repositorio cuenta con:
* [Bussiness](https://github.com/parkingmanager/ClientApp/tree/main/Bussiness): Una capa de negociación donde se analiza y estructura la información, para que pueda ser adaptada a la capa de integración.
* [Filters](https://github.com/parkingmanager/ClientApp/tree/main/Filters): En esta carpeta se diseñan las secciones de filtrado y procesamiento a través de:
  * Delimitación (Delimite.py): Se eligen manualmente las ROI sobre las cuales se aplicará el procesamiento.
  * Color (Color.py): En formato HSV se alteran las propiedades de colorimetría del Frame.
  * Transformada Libre o manual (Transform.py): Con los datos extraídos de un pixel en la imagen bicolor, se logra eliminar una zona específica o diseñar unan figura a través de líneas rectas.
  * Transformada de perspectiva y de Hough (TPerspective.py): Aplicando la transformada de perspectiva para cada ROI generada de forma manual, se busca aplica la Transformada de Hough, la cual permite reconstruir figuras geométricas, en este caso líneas rectas.
  * Búsqueda (SpaceConfig.py): Manualmente se seleccionan los espacios que se caracterizan como uso exclusivo.
 Integration: La capa de integración es la encarga de acoplar la aplicación al API REST.
 * [Models](https://github.com/parkingmanager/ClientApp/tree/main/Models): Sección para adquirir la información que debe ser almacenada durante un proceso específico.
 * [QTGraphicInterfaces](https://github.com/parkingmanager/ClientApp/tree/main/QTGraphicInterfaces): Se almacena el código fuente de la interfaz gráfica.
 * [Windows](https://github.com/parkingmanager/ClientApp/tree/main/Windows): Contiene los códigos fuentes de las principales funciones de la aplicación como:
   * Edición (Editor.py). Calibración y obtención coordenadas.
   * Transacción (Transactions.py y TransactionsForm.py). Através de OCR o teclado se obtienen características del vehículo ejerciendo un control administrativo sobre el tiempo de uso. 
   * Monitoreo (Visor.py). Predicción de estado de los espacios a través de una CNN. El código fuente para la extracción de datos de entrenamiento y el código de entrenamiento de la CNN puede encontrarlo en el reporsitorio de [Utils](https://github.com/parkingmanager/Utils.git)
   * Estadísticas (Stats.py). Uso de información extraída a través del monitoreo y de las transacciones.
 * [Main](https://github.com/parkingmanager/ClientApp/blob/main/main.py): Como el archivo que mapea la información y desde el cual se corre el proyecto.
 
 ### Herramientas de Implementación
 
 | [<img src="https://user-images.githubusercontent.com/82679673/195237078-29332f54-0a5c-401e-bfba-48da95a3fd24.png" width=100 height=80><br><sub>PyCharm 2021.2.3 </sub>](https://www.jetbrains.com/pycharm/download/#section=windows) |  [<img src="https://user-images.githubusercontent.com/82679673/195236725-db9ef122-ccfe-4762-93d6-906e386a51db.png" width=115><br><sub>PyQT5</sub>](https://build-system.fman.io/qt-designer-download)|  [<img src="https://user-images.githubusercontent.com/82679673/195236726-7545f608-73a5-43b8-a1ea-f4c263f5316b.png" width=145 height=80><br><sub>Anaconda 3 2021.05</sub>](https://www.anaconda.com/products/distribution) |
| :---: | :---: | :---: |

### Instalación.

#### Instalar Interprete

1. Descargamos el archivo .yml que se encuentra en la carpeta de [ClientApp/Environments](https://github.com/parkingmanager/ClientApp/tree/main/Environments)
2. Se realiza la instalación del entorno o interprete. Esta se lleva a cabo en Anaconda 3. 
 <p align="center">
 <img src="https://user-images.githubusercontent.com/82679673/195238349-d48a10d9-ac3d-4af9-ac9e-4d94ae711dc1.jpg" width=500><br><sub>
 </p>
 
 Vamos a la sección de Entornos o "Enviroments".
 
3. Buscamos la opción de importar.
 <p align="center">
 <img src="https://user-images.githubusercontent.com/82679673/195238641-8720a10a-4ba7-496f-a5c0-e11a0c83bcf6.jpg" width=500><br><sub>
 </p>
4. Importamos el archivo.
  <p align="center">
 <img src="https://user-images.githubusercontent.com/82679673/195238800-982b7e47-26d5-4c7a-a687-ca8f291fbd7b.jpg" width=500><br><sub>
</p>
#### Configurar el Intérprete en PyCharm

1. En la parte inferior de la ventana de PyCharm se encuentra el intérprete elegido por defecto.
<p align="center">
<img src="https://user-images.githubusercontent.com/82679673/195239140-7a7def75-2684-40f8-8985-ca5bd88b239c.jpg" width=500><br><sub>
 </p>
 2. Para adicionar o configurar el interprete, se da click izquierdo sobre el espacio.
 <p align="center">
<img src="https://user-images.githubusercontent.com/82679673/195239326-66d180a7-e656-4053-ae1e-c9fbcdcca0a7.jpg" width=500><br><sub>
</p>
3. En la nueva ventana desde la opción de anaconda, se debe seleccionar entorno existente y buscar la dirección sobre la cual se ha instalado.
<p align="center">
<img src="https://user-images.githubusercontent.com/82679673/195239544-3e5e4d53-af50-470b-b3b6-dfbc2f1046a5.jpg" width=500><br><sub>
</p>

#### Visite los repositorios de [DB](https://github.com/parkingmanager/Database.git) y [RestAPI](https://github.com/parkingmanager/RestAPI.git) para poder correr el proyecto.



