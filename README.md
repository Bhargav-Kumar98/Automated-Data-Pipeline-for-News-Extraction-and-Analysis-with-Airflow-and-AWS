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

<img width="648" alt="NewsAPI_Data_Engineeering_Pipeline" src="https://github.com/user-attachments/assets/1e9e96d1-f24a-49c1-be05-e9fe9e3483f9">

* Integrated the News API into the pipeline to fetch real-time news data regularly.

* Orchestrated the entire data pipeline using Apache Airflow, connecting to PostgreSQL for task management and utilizing Celery for distributed task execution.

* Stored metadata and task logs in PostgreSQL, supporting Apache Airflow operations.

* Handled distributed task execution within the pipeline using Celery.

* Containerized the entire pipeline with Docker, including Airflow, PostgreSQL, and Celery, to ensure consistent performance across different platforms.
  
<img width="1120" alt="dag success" src="https://github.com/user-attachments/assets/3c90816f-78c2-4eac-9204-4ceb4a9c2b8d">

* Stored data fetched from the News API in Amazon S3, both before and after transformation.
<img width="1120" alt="s3 raw" src="https://github.com/user-attachments/assets/11994a4d-e4b9-47bd-9757-69ff7cc194fb">

* Analyzed data stored in Amazon S3 using Amazon Athena, leveraging a serverless query service without loading data into a database.

<img width="1120" alt="glue job 1" src="https://github.com/user-attachments/assets/dfa75c0c-16cc-44cd-8468-99391a83f99f">


<img width="1119" alt="Glue job 2" src="https://github.com/user-attachments/assets/97877148-f344-4a92-badb-74ac790005c7">


<img width="1114" alt="transformed data" src="https://github.com/user-attachments/assets/78cd6f29-f8e2-49f6-ad50-01b67c91b2d5">


<img width="1120" alt="Crawler_un" src="https://github.com/user-attachments/assets/c3facefa-8d66-4379-9692-6a82872c621f">


<img width="1117" alt="athena" src="https://github.com/user-attachments/assets/ce13e3d5-b9b6-4a69-9bfd-5387e7fd2378">

* Transformed and loaded data into Amazon Redshift using AWS Glue, connecting raw and transformed data in S3 with the data catalog. 

<img width="1120" alt="redshift-1" src="https://github.com/user-attachments/assets/7d22a463-0e06-41b4-a150-8ce2c34e2ed2">


<img width="1120" alt="redshift" src="https://github.com/user-attachments/assets/cbf645cf-c62b-4bc0-965e-7e14ad1cbff6">


## What I have learnt?

* Gained hands-on experience in orchestrating complex data pipelines using Apache Airflow, including task management and scheduling.

* Mastered Docker to containerize various components of the pipeline, ensuring consistent performance and easy deployment across environments.

* Developed a deep understanding of ETL processes using AWS Glue for transforming and loading data, connecting S3 storage with data cataloging and Redshift.

* Acquired skills in storing and analyzing large datasets in Amazon S3, Athena, and Redshift, optimizing for scalable and efficient querying.

* Enhanced proficiency in integrating APIs into data pipelines, specifically for fetching and processing real-time data.
