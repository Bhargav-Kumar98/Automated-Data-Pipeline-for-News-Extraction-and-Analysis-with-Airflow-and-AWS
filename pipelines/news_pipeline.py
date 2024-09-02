import pandas as pd

from etls.news_etl import connect_to_news_api, extract_headlines, transform_data, load_data_to_csv
from utils.constants import NEWS_API_KEY, OUTPUT_PATH
import json


def news_pipeline(file_name: str, time_filter, limit=None):
    # Connecting to news api instance
    instance = connect_to_news_api(NEWS_API_KEY)
    
    # Extraction
    response = extract_headlines(instance)
    
    # Transformation
    news_df = transform_data(response)

    # Load to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(news_df, file_path)
    
    return file_path