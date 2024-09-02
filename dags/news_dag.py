import os
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.news_pipeline import news_pipeline

default_args = {
    'owner': 'Bhargav Kumar Aathava',
    'start_date': datetime(2024, 8, 31)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='news_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['news', 'etl', 'pipeline']
)

# Extraction from news api
extract = PythonOperator(
    task_id='news_extraction',
    python_callable=news_pipeline,
    op_kwargs={
        'file_name': f'top_headlines_{file_postfix}',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

# upload to aws s3
upload_to_s3 = PythonOperator(
    task_id='uploading_to_aws_s3',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_to_s3