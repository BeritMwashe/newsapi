class Config:
    NEWS_BASE_URL='https://newsapi.org/v2/top-headlines?country=kenya&apiKey={}'
    NEWS_BASE_EVERYTHING_URL='https://newsapi.org/v2/everything?q={}&from=2021-08-07&sortBy=popularity&apiKey={}'
    NEWS_BASE_URL_SOURCES='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_EVERYTHING_SOURCES='https://newsapi.org/v2/everything?domains={}&apiKey={}'
class ProdConfig(Config):
    pass


class DevConfig(Config):
    pass