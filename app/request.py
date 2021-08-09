# from app.test_sources import Source

from .models import Articles
from .models import Sources
# from app import app
import urllib.request,json
#api




# api_key=app.config['NEWS_API_KEY']
# base_url=app.config["NEWS_BASE_URL_SOURCES"]
# base_url_for_everything=app.config['NEWS_BASE_EVERYTHING_URL']
# base_url_top_headlines=app.config['NEWS_BASE_HEADLINES_URL']
# base_source_list=app.config['NEWS_BASE_SOURCE']

api_key=None
base_url=None
base_url_for_everything=None
base_url_top_headlines=None
base_source_list=None

def configure_request(app):
    global api_key,base_url,base_url_for_everything,base_url_top_headlines,base_source_list
  
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config["NEWS_BASE_URL_SOURCES"]
    base_url_for_everything=app.config['NEWS_BASE_EVERYTHING_URL']
    base_url_top_headlines=app.config['NEWS_BASE_HEADLINES_URL']
    base_source_list=app.config['NEWS_BASE_SOURCE']




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

        if name!=('ANSA.it'):
            source_object=Sources(id,name,description,url,country,language)

            source_results.append(source_object)
    return source_results

def get_Articles(domain):
    articles_url=base_url_for_everything.format(domain,api_key)
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
    if article_result_list:
        for article in article_result_list:
            source=article.get('source')
            author=article.get('author')
            title=article.get('title')
            description=article.get('description')
            url=article.get('url')
            urlToImage=article.get('urlToImage')
            publishedAt=article.get('publishedAt')
            content=article.get('content')


            if urlToImage:
                article_object=Articles(source,author,title,description,url,urlToImage,publishedAt,content)
                article_results.append(article_object)
        return article_results
    else:
        return '<h1>nothing to display</h1>'
def get_headlines():
    articles_url=base_url_top_headlines.format(api_key)
    with urllib.request.urlopen(articles_url) as url:
        articles_url_data=url.read()
        articles_url_response=json.loads(articles_url_data)


        headlines_results=None


        if articles_url_response['articles']:
            print("available")
            articles_results_list=articles_url_response['articles']
            headlines_results=process_article_results(articles_results_list)


    return headlines_results


def get_articles_sos(source):
    articles_url=base_source_list.format(source,api_key)
    with urllib.request.urlopen(articles_url) as url:
        articles_url_data=url.read()
        articles_url_response=json.loads(articles_url_data)


        articles_results=None


        if articles_url_response['articles']:
            print("available")
            articles_results_list=articles_url_response['articles']
            articles_results=process_article_results(articles_results_list)
        else:
            articles_results=process_article_results(articles_results)

    return articles_results