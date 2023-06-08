
# <h1 align=center> **Final Project - Sismic Alerts** </h1>
                                            

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/logo.jpeg"  height=300>
</p>

--- 
### Welcome to the earthquake data analysis project for an insurance company! We are pleased to present the results of our collaborative work on this exciting project.
---
## `Team`
We have a highly collaborative team composed of 5 members, each with specific roles and distinct approaches:

#### Data Engineer :
+ Matias Trovatto ( [Github](https://github.com/MatyTrova) - [LinkedIn](https://www.linkedin.com/in/matias-trovatto-b33972255/) )
+ Rene Ramos  ( [Github](https://github.com/ReneRamosTrvn) - [LinkedIn](https://www.linkedin.com/in/ren%C3%A9-ramos-669536194/) )

#### Data Analysts :
+ Victoria Rios ( [Github](https://github.com/QuimeraRios) - [LinkedIn](https://www.linkedin.com/in/victoria-rios-datascience/) )
+ Jose Jimenez ( [Github](https://github.com/josej16) - [LinkedIn](https://www.linkedin.com/in/jos%C3%A9-antonio-jim%C3%A9nez-tob%C3%ADa-77914913b/) )

#### Machine Learning Developer :
+ Iván Diaz  ( [Github](https://github.com/Ivancadi) - [LinkedIn](https://www.linkedin.com/in/ivan-diaz-ca%C3%B1avera-739124211/) )

## `About the project:`
This project has been carried out in collaboration with an insurance company specializing in life and property policies. Our main objective has been to analyze and understand the impacts of earthquakes globally, providing valuable information to improve the company's strategies and decision-making.

To achieve this, we have followed an agile methodology, using sprints to organize our activities and ensure an efficient workflow. Each sprint had a fixed duration, and we focused on clear and achievable goals within that timeframe.

We implemented a cloud-based database using Google Cloud, which allowed us to efficiently store and manage earthquake and insurance sales data. We applied extraction, transformation, and loading (ETL) techniques, as well as exploratory data analysis (EDA) to identify relevant patterns, trends, and correlations.

During the ETL process, we used various techniques, such as iterating through an API to obtain real-time data and web scraping to complement information from public sources. This provided us with a comprehensive and up-to-date dataset for our analyses.

Additionally, we developed an interactive dashboard using Power BI to present the results. This dashboard offers clear and concise visualizations, facilitating the understanding of patterns, trends, and correlations between earthquakes and insurance sales. We also applied machine learning techniques to develop predictive models for earthquake occurrence and intensity, enabling the company to take preventive measures and adjust their insurance strategies proactively.

We are excited to share the results of our analysis through this dashboard and hope it becomes a valuable tool for the company, helping them make informed decisions and provide quality insurance services to their clients.

[Video](https://youtu.be/6GYkmYvxhkw)


## `Repository Structure:`

- [README.md](./README.md) : Main file with all info about the project.

- [Datasets](./Datasets) : This folder contains all datasets used in this project.

- [Datasets_csv](./Datasets_csv) : This folder contains all datasets used in this project in CSV format.

- [ML](./ML) : Folder that contains all assets for the Machine Learning model.

- [driver](./driver) :Contains driver to use Web Scrapping.

- [imgs](./imgs) : Contains all images.

- [Gantt diagram](./DiagramaGanttAlertasSismicas.xlsx) : Contains Gantt's diagram that shows prpject trajectory.

- [ETL](./ETL.ipynb) : Python Notebook that contains all Extraction, Transformation and Load (ETL) process.

- [EDA](./EDA.ipynb) : Python Notebook that contains all Exploratory Data Analysis (EDA).

## `Data Life Cycle` 

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/diagrama%20ciclo%20de%20dato.jpeg"  alt="Final">
</p>

## `Entity-Relation diagram` 

<p align="center">
  <img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/Diagrama%20ER.svg" width="1000" height="400">
</p>



## `Flowchart` 

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/31db1805ab784cdcc2b9a5c4bc3f9fe2QhQnD9gQr9oyACnz-0.png" >
</p>

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/31db1805ab784cdcc2b9a5c4bc3f9fe2QhQnD9gQr9oyACnz-1.png" >
</p>

---

## `Data Engineering` 
The Data Engineer team was responsible for carrying out the entire process of Extraction, Transformation, and Loading (ETL) of the data. Initially, the necessary data sources were identified, including an API, web pages, Excel files, and JSON. Once access to these sources was obtained, the data extraction process began.

Data extraction was primarily performed using Python as the main tool. A fully documented and explained Python notebook was developed, detailing the steps and logic behind each extraction. Various techniques were used in this stage, such as iterating through an API, web scraping on multiple pages and data merging, as well as reading Excel and JSON files. Each of these processes is described step by step in the corresponding notebook. During web scraping, the team encountered some challenges, but through teamwork, they were resolved, and the established objectives were met.

Once all the data tables were obtained, an Exploratory Data Analysis (EDA) was conducted to identify relevant patterns, trends, and correlations. This analysis was carried out using Python as the main tool, allowing for a more detailed examination of each table in the database.

The EDA provided a deeper understanding of the data, revealing valuable information about the characteristics and distribution of the data in each table. Through visualization techniques and descriptive statistics, emerging patterns, significant trends, and possible relationships between variables were identified.

This exploratory process provided the team with a solid understanding of the nature of the data, which helped in making informed decisions in subsequent data analysis and modeling. A series of transformations were then applied to ensure data quality. These transformations included standardizing and normalizing the tables, removing columns that did not add value, aggregating identification columns, and extracting dimensional tables to improve the overall structure of the data.

Finally, the resulting 33 files were exported in two formats: JSON for further processing and CSV to facilitate cloud work and enable easier data handling.

Additionally, the infrastructure was configured in Google Cloud Platform (GCP), integrating the transformation code into the environment and ensuring the proper execution of the ETL process. The result was an automated and efficient data flow, with the transformed data loaded into BigQuery's data warehouse, ready to be analyzed by the Data Analytics team.

---

## `Data Analytics` 


The selection process for the KPIs initially started with 5 key indicators but was later refined to 4 KPIs after several iterations. These KPIs focused on the following aspects:

+Increase in property insurance policies.
+Increase in life insurance policies.
+Increase in participants in drills/simulations.
+Reduction in fatalities in seismic events.

The KPIs related to property and life insurance policies proved to be particularly useful as high-quality information was available to measure their performance. For the drill/simulation and fatalities KPIs, web scraping techniques were employed to gather relevant data.

The development and explanation of these KPIs were aligned with the interests of an insurance company, aiming to find ways to increase revenue and reduce losses. Attention was also given to visual aspects, such as a visually pleasing color palette, proper positioning of charts, and clear definition of titles, ensuring that the entire dashboard was easily understandable at a glance.

The fatalities KPI proved to be of vital importance in reducing claims losses for life insurance. A negative correlation was observed between the increase in policies and the decrease in fatalities. Additionally, the drill/simulation participation KPI played a crucial role in contributing to the reduction of fatalities in the event of earthquakes. This decrease in fatalities resulted in a reduction in death claims payments associated with seismic events.

The analysis of the property insurance KPI for an insurance company is promising as it allows determining the frequency and location of earthquakes, as well as identifying areas that need insurance coverage. The Japanese government encourages the acquisition of insurance for earthquake-resistant homes. Opportunities were found to offer policies in areas with a high frequency of earthquakes but low insurance acquisition.

Regarding life insurance policies, it was observed that on average, three people are covered by each policy, indicating a family-oriented approach rather than an individual one. Offering family policies and considering coverage for outpatient visits, which are the most frequent claims, is recommended.

Despite the pandemic, the insurance sector had experienced significant growth in the acquisition of property and life insurance policies. This represents coverage of 83% in relation to the population of Japan.

In summary, the analysis of the KPIs allows for the identification of seismic risk areas and the insurance approaches that should be offered. Additionally, a focus on family policies and considering coverage for outpatient visits in life insurance policies is recommended. Despite the pandemic, the insurance sector had solid growth in the acquisition of policies.

---

## `Machine Learning` 

A machine learning model has been implemented using the K-means algorithm. The process begins with an exploratory analysis of the data, where relevant variables such as depth, magnitude, and seismic wave amplitude are studied. Through visualization techniques, patterns and trends in the data are identified.

Next, data evaluation is conducted using two methods: the Elbow method and the Silhouette index. These methods help determine the optimal number of clusters for the K-means model and evaluate the quality of the resulting clustering. The results are compared with the initial choice of 3 clusters to validate the robustness of the model.

Once the number of clusters is defined, the K-means algorithm is applied to the data and the model is trained. To visualize the results in a graphical manner, the dimensionality reduction technique called Principal Component Analysis (PCA) is used. This projects the data into a two-dimensional space, allowing the clusters to be represented on a 2D graph and visualizing the distribution of earthquakes according to their hazard level.

Finally, the model is put into production by implementing a user interface using Streamlit. Users can interact with the interface and provide the characteristics of an earthquake (depth, magnitude, and seismic wave amplitude) through sliders. The real-time applied model provides a prediction of the earthquake's hazard level, indicating whether it is of low, medium, or high hazard.

---

## `Dashboard` 
---

+ KPIs
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/portada.png"  alt="Final">
</p>


---

+ Increase in property insurance policies
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag%201.png"  alt="Final">
</p>


---

+ Increase in life insurance policies
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag2.png"  alt="Final">
</p>


---

+ Increase in participation in drills/simulations
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag3.png"  alt="Final">
</p>

---

+ Reduction in fatalities
<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/pag4.png"  alt="Final">
</p>


---

##### Note: To access all the files, including the dashboard, you can go to the following Google Drive link: 
( [Link](https://drive.google.com/drive/folders/1i0_Jir644PRO1j7tAGKSgVmxJ0_9C6KL) )

---

<p align="center">
<img src="https://github.com/ReneRamosTrvn/alertas_sismicas/blob/main/imgs/henry.jpg"  alt="Final">
</p>


