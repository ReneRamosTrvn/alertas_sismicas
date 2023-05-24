
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

- [Diagrama de Gantt](./DiagramaGanttAlertasSismicas.xlsx) : Contiene el diagrama de Gantt que muestra la trayectoria del proyecto.

- [ETL](./ETL.ipynb) : Notebook de python que contiene todo el código para la extracción, transformación y carga de los datos.

- [EDA](./EDA.ipynb) : Notebook de python que contiene todo el código para el análisis exploratorio de datos.

## `Ciclo de vida del dato` 

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/diagrama%20ciclo%20de%20dato.jpeg"  alt="Final">
</p>

## `Diagrama entidad-relación` 

<p align="center">
  <img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/Diagrama%20ER.svg" width="1000" height="400">
</p>



## `Diagrama de flujo` 

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/31db1805ab784cdcc2b9a5c4bc3f9fe2QhQnD9gQr9oyACnz-0.png" >
</p>

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/31db1805ab784cdcc2b9a5c4bc3f9fe2QhQnD9gQr9oyACnz-1.png" >
</p>

---

## `Data Engineer` 
El equipo de Data Engineer se encargó de llevar a cabo todo el proceso de Extracción, Transformación y Carga (ETL) de los datos. Inicialmente, se identificaron las fuentes de datos necesarias, las cuales incluían una API, páginas web, archivos Excel y JSON. Una vez que se obtuvo acceso a estas fuentes, se procedió a la extracción de los datos.

La extracción de datos se llevó a cabo principalmente utilizando Python como la herramienta principal. Se desarrolló un notebook de Python completamente documentado y explicado, el cual detalla los pasos y la lógica detrás de cada extracción. Se utilizaron diversas técnicas en esta etapa, como la iteración a través de una API, el web scraping en varias páginas y la combinación de los datos, así como la lectura de archivos Excel y JSON. Cada uno de estos procesos se describe paso a paso en el correspondiente notebook. Durante el web scraping, el equipo se enfrentó a algunos desafíos, pero gracias al trabajo en equipo, se lograron resolver y cumplir con los objetivos establecidos.

Una vez que se obtuvieron todas las tablas de datos, se realizó un Análisis Exploratorio de Datos (EDA, por sus siglas en inglés) con el objetivo de identificar patrones, tendencias y correlaciones relevantes. Este análisis se llevó a cabo utilizando Python como herramienta principal, lo que permitió examinar más detalladamente cada tabla de la base de datos.

El EDA proporcionó una visión más profunda de los datos, revelando información valiosa sobre las características y distribución de los datos en cada tabla. Mediante técnicas de visualización y estadísticas descriptivas, se lograron identificar patrones emergentes, tendencias significativas y posibles relaciones entre las variables.

Este proceso de exploración brindó al equipo una comprensión más sólida de la naturaleza de los datos, lo que ayudó a tomar decisiones fundamentadas en el posterior análisis y modelado de datos. A continuación, se aplicaron una serie de transformaciones para asegurar la calidad de los mismos. Estas transformaciones incluyeron la estandarización y normalización de las tablas, la eliminación de columnas que no aportaban valor, la agregación de columnas de identificación y la extracción de tablas dimensionales para mejorar la estructura general de los datos.

Finalmente, se exportaron los 33 archivos resultantes en dos formatos: JSON, para su posterior procesamiento, y CSV, para facilitar el trabajo en la nube y permitir un manejo más sencillo de los datos.

Además, se configuró la infraestructura en Google Cloud Platform (GCP), integrando el código de transformación en el entorno y garantizando la correcta ejecución del proceso ETL. El resultado fue un flujo de datos automatizado y eficiente, con los datos transformados y cargados en el data warehouse de BigQuery, listos para ser analizados posteriormente por el equipo de Data Analytics.

---

## `Data Analytics` 

El proceso de selección de los KPIs se basó inicialmente en 5 indicadores clave, pero después de varias correcciones, se redujo a 4 KPIs. Estos KPIs se centraron en los siguientes aspectos:

+ Aumento de las pólizas de inmuebles.
+ Aumento de las pólizas de vida.
+ Aumento de participantes en simulacros.
+ Reducción de fatalidades en eventos sísmicos.

Los KPIs relacionados con las pólizas de inmuebles y vida resultaron especialmente útiles, ya que se obtuvo información de alta calidad para medir su desempeño. En el caso de los KPIs de simulacros y fatalidades, se requirió utilizar técnicas de web scraping para recopilar datos relevantes.

El desarrollo y la explicación de estos KPIs se orientaron a los intereses de una empresa aseguradora, con el objetivo de encontrar formas de aumentar los ingresos y reducir las pérdidas. Además, se prestó atención a aspectos visuales, como una paleta de colores agradable a la vista, un posicionamiento adecuado de los gráficos y una clara definición de los títulos, con el fin de que todo el dashboard fuera fácilmente comprensible a simple vista.

El KPI de fatalidades resultó ser de vital importancia para reducir las pérdidas por reclamos de muerte en seguros de vida. Se observó una correlación negativa entre el aumento de pólizas y la disminución de fatalidades. Además, el KPI de aumento de participantes en simulacros desempeñó un papel fundamental, ya que contribuyó a reducir las fatalidades en caso de sismos. Esta disminución en las fatalidades resultó en una reducción de los pagos de reclamos por muerte asociados a eventos sísmicos

El análisis del KPI de inmuebles para una empresa de seguros es prometedor, ya que permite determinar la frecuencia y ubicación de los sismos, así como identificar las áreas que necesitan adquirir seguros. El gobierno de Japón incentiva la adquisición de seguros para viviendas con resistencia sísmica. Se encontraron oportunidades para ofrecer pólizas en áreas con alta frecuencia de sismos pero baja adquisición de seguros.

En cuanto a las pólizas de vida, se observó que en promedio hay tres personas cubiertas por cada póliza, lo que indica un enfoque familiar en lugar de individual. Se recomienda ofrecer pólizas familiares y considerar coberturas para visitas ambulatorias, ya que son los reclamos más frecuentes.

A pesar de la pandemia, el sector de seguros había experimentado un crecimiento considerable en la adquisición de pólizas de inmuebles y vida. Esto representa una cobertura del 83% en relación a la población de Japón.

En resumen, el análisis de los KPIs permite identificar las áreas de riesgo sísmico y los enfoques de pólizas que se deben ofrecer. Además, se recomienda enfocarse en pólizas familiares y considerar coberturas para visitas ambulatorias en las pólizas de vida. A pesar de la pandemia, el sector de seguros había experimentado un crecimiento sólido en la adquisición de pólizas.

---

## `Machine Learning` 

Se ha implementado un modelo de machine learning utilizando el algoritmo K-means. El proceso comienza con un análisis exploratorio de los datos, donde se estudian las variables relevantes como la profundidad, magnitud y amplitud de ondas sísmicas. A través de técnicas de visualización, se identifican patrones y tendencias en los datos.

Luego, se lleva a cabo una evaluación de los datos utilizando dos métodos: el Codo de Jambu (Elbow) y el índice de silueta (Silhouette). Estos métodos permiten determinar el número óptimo de clusters para el modelo de K-means y evaluar la calidad del agrupamiento obtenido. Se comparan los resultados con la elección inicial de 3 clusters para validar la robustez del modelo.

Una vez definido el número de clusters, se aplica el algoritmo K-means a los datos y se entrena el modelo. Para visualizar los resultados de manera gráfica, se utiliza la técnica de reducción de dimensionalidad llamada PCA, que proyecta los datos en un espacio bidimensional. Esto permite representar los clusters en un gráfico 2D y visualizar la distribución de los sismos según su peligrosidad.

Finalmente, el modelo se lleva a producción mediante la implementación de una interfaz de usuario utilizando Streamlit. Los usuarios pueden interactuar con la interfaz y proporcionar las características de un sismo (profundidad, magnitud y amplitud de ondas sísmicas) a través de sliders. El modelo aplicado en tiempo real proporciona una predicción sobre la peligrosidad del sismo, indicando si es de baja, media o alta peligrosidad.

---

## `Dashboard` 
A continuación se adjuntan las imágenes del respectivo dashboard
---

+ KPIs
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/portada.png"  alt="Final">
</p>


---

+ Aumento de pólizas de inmuebles
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag%201.png"  alt="Final">
</p>


---

+ Aumento de pólizas de vida
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag2.png"  alt="Final">
</p>


---

+ Aumento de participación en simulacros
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag3.png"  alt="Final">
</p>

---

+ Disminución de fatalidades
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag4.png"  alt="Final">
</p>


---

##### Nota: Para acceder a todos los archivos, incluido el dashboard, se puede ingresar al siguiente enlace de drive : 
( [Link al drive](https://drive.google.com/drive/folders/1i0_Jir644PRO1j7tAGKSgVmxJ0_9C6KL) )

---

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/henry.jpg"  alt="Final">
</p>


