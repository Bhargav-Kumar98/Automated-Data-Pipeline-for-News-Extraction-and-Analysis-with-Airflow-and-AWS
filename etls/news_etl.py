from newsapi import NewsApiClient
import json
import sys
import pandas as pd

def connect_to_news_api(news_api_key):
    try:
        newsapi = NewsApiClient(api_key=news_api_key)
        print("connected to News Api!")
        return newsapi
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_headlines(instance):
    try:
        response = instance.get_top_headlines(category='business', language='en', country='us', page_size=30)
        print("Extracted data from News Api!")
        return response
    except Exception as e:
        print(e)
        sys.exit(1)
    
def transform_data(response):
    news_df = pd.DataFrame(response['articles'])
    return news_df[['author', 'title', 'url']]

def load_data_to_csv(news_df, file_path):
    news_df.to_csv(file_path, index=False)