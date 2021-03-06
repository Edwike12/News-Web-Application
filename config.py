
import os

    
class Config:
    """
    General configuration parent class
    """
    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = 'ea1ea4db45ad44dbb126fe10de6b89fe'
    
   
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}