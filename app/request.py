# from app.test_sources import Source

from .models import articles
from .models import sources
from app import app
import urllib.request,json
#api

Source=sources.Sources
Articles=articles.Articles

api_key=app.config['NEWS_API_KEY']
base_url=app.config["NEWS_BASE_URL_SOURCES"]
base_url_for_everything=app.config['NEWS_BASE_EVERYTHING_URL']




# getting the request
def get_sources():
    sources_url=base_url.format(api_key)
    with urllib.request.urlopen(sources_url) as url:
        sources_url_data=url.read()
        sources_url_response=json.loads(sources_url_data)


        source_results=None


        if sources_url_response['sources']:
            print("availabel")
            source_results_list=sources_url_response['sources']
            source_results=process_results(source_results_list)


    return source_results


def process_results(sources_list):
    source_results=[]
    for source in sources_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        country=source.get('country')
        language=source.get('language')


        source_object=Source(id,name,description,url,country,language)

        source_results.append(source_object)
    return source_results

def get_Articles(category='everything',query='all'):
    articles_url=base_url_for_everything.format(category,query,api_key)
    with urllib.request.urlopen(articles_url) as url:
        articles_url_data=url.read()
        articles_url_response=json.loads(articles_url_data)


        articles_results=None


        if articles_url_response['articles']:
            print("available")
            articles_results_list=articles_url_response['articles']
            articles_results=process_article_results(articles_results_list)


    return articles_results

def process_article_results(article_result_list):
    article_results=[]
    for article in article_result_list:
        source=article.get('source')
        author=article.get('author')
        title=article.get('title')
        description=article.get('description')
        url=article.get('url')
        urlToImage=article.get('urlToImage')
        publishedAt=article.get('publishedAt')
        content=article.get('content')
        article_object=Articles(source,author,title,description,url,urlToImage,publishedAt,content)
        article_results.append(article_object)
    return article_results
