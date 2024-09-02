# Data-Engineering-Pipeline-for-News-Data-Extraction-and-Analysis

## Project Overview
This project focuses on building a scalable and automated data engineering pipeline that extracts data from a News API, processes it using Apache Airflow, and stores it in AWS services for further analysis. 

The architecture includes various components like PostgreSQL, Celery, Docker, AWS Glue, Amazon S3, Amazon Athena, and Amazon Redshift. 

The goal of this project is to create a robust and efficient data pipeline for collecting, processing, and analyzing news data.

## Technologies used:
* Python
* Apache Airflow
* Docker
* AWS Glue
* Amazon S3
* Amazon Athena
* Amazon Redshift
* PostgreSQL

## System Architecture

<img width="648" alt="NewsAPI_Data_Engineeering_Pipeline" src="https://github.com/user-attachments/assets/a7c8ace1-13b1-4e57-9a48-94c5b3a23061">

* Integrated the News API into the pipeline to fetch real-time news data regularly.

* Orchestrated the entire data pipeline using Apache Airflow, connecting to PostgreSQL for task management and utilizing Celery for distributed task execution.

* Stored metadata and task logs in PostgreSQL, supporting Apache Airflow operations.

* Handled distributed task execution within the pipeline using Celery.

* Containerized the entire pipeline with Docker, including Airflow, PostgreSQL, and Celery, to ensure consistent performance across different platforms.
  
<img width="1120" alt="dag success" src="https://github.com/user-attachments/assets/3c90816f-78c2-4eac-9204-4ceb4a9c2b8d">

* Stored data fetched from the News API in Amazon S3, both before and after transformation.
<img width="1120" alt="s3 raw" src="https://github.com/user-attachments/assets/d4a5135b-f3f8-4d15-b7a6-8d499775b8b6">

* Analyzed data stored in Amazon S3 using Amazon Athena, leveraging a serverless query service without loading data into a database.

<img width="1119" alt="Glue job 1" src="https://github.com/user-attachments/assets/d6b50b16-6efb-454a-bbb8-967d1ba6eb17">

<img width="1120" alt="glue job 2" src="https://github.com/user-attachments/assets/a42ffc65-5845-422d-9be7-fc3795174dc4">

<img width="1114" alt="transformed data" src="https://github.com/user-attachments/assets/cc583f52-cbc0-4d04-b81c-fa5a90fdffe6">

<img width="1120" alt="Crawler_un" src="https://github.com/user-attachments/assets/dc55ff1d-a4a6-4f60-a43b-ae0caf5a2737">

<img width="1117" alt="athena" src="https://github.com/user-attachments/assets/4ddac07a-1495-4cec-b4c2-e0fe3b198096">

* Transformed and loaded data into Amazon Redshift using AWS Glue, connecting raw and transformed data in S3 with the data catalog. 

<img width="1120" alt="redshift-1" src="https://github.com/user-attachments/assets/1279d85d-2dab-4c13-98ee-d5958399a121">

<img width="1120" alt="redshift" src="https://github.com/user-attachments/assets/c23d36cb-5a73-43f3-9f99-068debc944b3">


## What I have learnt?

* Gained hands-on experience in orchestrating complex data pipelines using Apache Airflow, including task management and scheduling.

* Mastered Docker to containerize various components of the pipeline, ensuring consistent performance and easy deployment across environments.

* Developed a deep understanding of ETL processes using AWS Glue for transforming and loading data, connecting S3 storage with data cataloging and Redshift.

* Acquired skills in storing and analyzing large datasets in Amazon S3, Athena, and Redshift, optimizing for scalable and efficient querying.

* Enhanced proficiency in integrating APIs into data pipelines, specifically for fetching and processing real-time data.
