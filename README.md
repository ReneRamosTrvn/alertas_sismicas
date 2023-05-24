
# <h1 align=center> **Proyecto Final: Alertas sísmicas** </h1>
                                            

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/Earthquake%20safety%20steps%20with%20disaster%20emergency%20action%20advice%20outline%20diagram.jpg"  height=300>
</p>

--- 
### ¡Bienvenidos al proyecto de análisis de datos de sismos para una compañía de seguros! Nos complace presentar los resultados de nuestro trabajo colaborativo en este emocionante proyecto.
---
## `Equipo`
Contamos con un equipo altamente colaborativo compuesto por 5 integrantes, cada uno con roles específicos y enfoques particulares:

#### Data Engineer :
+ Matias Trovatto ( [Github](https://github.com/MatyTrova) - [LinkedIn](https://www.linkedin.com/in/matias-trovatto-b33972255/) )
+ Rene Ramos  ( [Github](https://github.com/ReneRamosTrvn) - [LinkedIn](https://www.linkedin.com/in/ren%C3%A9-ramos-669536194/) )

#### Data Analytics :
+ Victoria Rios ( [Github](https://github.com/QuimeraRios) - [LinkedIn](https://www.linkedin.com/in/victoria-rios-datascience/) )
+ Jose Jimenez ( [Github](https://github.com/josej16) - [LinkedIn](https://www.linkedin.com/in/jos%C3%A9-antonio-jim%C3%A9nez-tob%C3%ADa-77914913b/) )

#### Machine Learning :
+ Iván Diaz  ( [Github](https://github.com/Ivancadi) - [LinkedIn](https://www.linkedin.com/in/ivan-diaz-ca%C3%B1avera-739124211/) )

## `Descripción del proyecto`
Este proyecto se ha llevado a cabo en colaboración con una empresa de seguros especializada en pólizas de vida e inmuebles. Nuestro objetivo principal ha sido analizar y comprender los impactos de los sismos a nivel global, brindando información valiosa para mejorar las estrategias y la toma de decisiones de la empresa.

Para lograrlo, hemos seguido una metodología ágil de trabajo, utilizando sprints para organizar nuestras actividades y garantizar un flujo eficiente de trabajo. Cada sprint ha tenido una duración fija y nos hemos enfocado en metas claras y alcanzables dentro de ese marco de tiempo.

Hemos implementado una base de datos en la nube utilizando Google Cloud, lo que nos ha permitido almacenar y gestionar eficientemente los datos relacionados con sismos y ventas de seguros. Aplicamos técnicas de extracción, transformación y carga (ETL), así como análisis exploratorio de datos (EDA) para identificar patrones, tendencias y correlaciones relevantes.

Durante el proceso de ETL, utilizamos diversas técnicas, como la iteración en una API para obtener datos en tiempo real y el web scraping para complementar la información de fuentes públicas. Esto nos proporcionó un conjunto de datos completo y actualizado para nuestros análisis.

Además, desarrollamos un dashboard interactivo utilizando Power BI para presentar los resultados. Este dashboard ofrece visualizaciones claras y concisas, facilitando la comprensión de los patrones, tendencias y correlaciones entre los sismos y las ventas de seguros. También aplicamos técnicas de machine learning para desarrollar modelos predictivos de la ocurrencia y la intensidad de los sismos, permitiendo a la empresa tomar medidas preventivas y ajustar sus estrategias de seguros de manera proactiva.

Estamos entusiasmados por compartir los resultados de nuestro análisis a través de este dashboard y esperamos que sea una herramienta valiosa para la empresa, ayudándoles a tomar decisiones fundamentadas y ofrecer servicios de seguro de calidad a sus clientes.

## `Estructura del repositorio`

- [README.md](./README.md) : Archivo principal con información detallada del proyecto.

- [Datasets](./Datasets) : Contiene los data sets utilizados en el proyecto.

- [Datasets_csv](./Datasets_csv) : Contiene los data sets utilizados en el proyecto pero en formato CSV.

- [ML](./ML) : Carpeta que contiene todos los elementos para el desarrollo del modelo de Machine Learning.

- [driver](./driver) : Contiene el driver para realizar el Web Scrapping

- [imgs](./imgs) : Contiene las imágenes del proyecto.

- [ETL](./ETL.ipynb) : Notebook de python que contiene todo el código para la extracción, transformación y carga de los datos.

- [EDA](./EDA.ipynb) : Notebook de python que contiene todo el código para el análisis exploratorio de datos.

## `Diagrama entidad-relación` 

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/Diagrama%20ER.svg" >
</p>


## `Diagrama de flujo` 

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/31db1805ab784cdcc2b9a5c4bc3f9fe2QhQnD9gQr9oyACnz-0.png" >
</p>

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/31db1805ab784cdcc2b9a5c4bc3f9fe2QhQnD9gQr9oyACnz-1.png" >
</p>


## `Data Engineer` 

(breve explicación del trabajo del equipo de data eng)

## `Data Analytics` 

(breve expl del trabajo del equipo de data analytics)

## `Machine Learning` 

Se ha implementado un modelo de machine learning utilizando el algoritmo K-means. El proceso comienza con un análisis exploratorio de los datos, donde se estudian las variables relevantes como la profundidad, magnitud y amplitud de ondas sísmicas. A través de técnicas de visualización, se identifican patrones y tendencias en los datos.

Luego, se lleva a cabo una evaluación de los datos utilizando dos métodos: el Codo de Jambu (Elbow) y el índice de silueta (Silhouette). Estos métodos permiten determinar el número óptimo de clusters para el modelo de K-means y evaluar la calidad del agrupamiento obtenido. Se comparan los resultados con la elección inicial de 3 clusters para validar la robustez del modelo.

Una vez definido el número de clusters, se aplica el algoritmo K-means a los datos y se entrena el modelo. Para visualizar los resultados de manera gráfica, se utiliza la técnica de reducción de dimensionalidad llamada PCA, que proyecta los datos en un espacio bidimensional. Esto permite representar los clusters en un gráfico 2D y visualizar la distribución de los sismos según su peligrosidad.

Finalmente, el modelo se lleva a producción mediante la implementación de una interfaz de usuario utilizando Streamlit. Los usuarios pueden interactuar con la interfaz y proporcionar las características de un sismo (profundidad, magnitud y amplitud de ondas sísmicas) a través de sliders. El modelo aplicado en tiempo real proporciona una predicción sobre la peligrosidad del sismo, indicando si es de baja, media o alta peligrosidad.

## `Dashboard` 
A continuación se adjuntan las imágenes del respectivo dashboard
---
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/portada.png"  alt="Final">
</p>
+ KPIs
---
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag%201.png"  alt="Final">
</p>
+ Aumento de pólizas de inmuebles
---
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag2.png"  alt="Final">
</p>
+ Aumento de pólizas de vida
---
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag3.png"  alt="Final">
</p>
+ Aumento de participación en simulacros
---
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag4.png"  alt="Final">
</p>
+ Disminución de fatalidades
---
##### Nota: Para acceder a todos los archivos, incluido el dashboard, se puede ingresar al siguiente enlace de drive : 
( [Link al drive](https://drive.google.com/drive/folders/1i0_Jir644PRO1j7tAGKSgVmxJ0_9C6KL) )
---

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/henry.jpg"  alt="Final">
</p>


