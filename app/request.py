from app import app
import urllib.request,json
#api


api_key=app.config['NEWS_API_KEY']
base_url=app.config["NEWS_BASE_URL_SOURCES"]




# getting the request
def get_sources():
    sources_url=base_url+api_key
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
    for source in sources_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        language=source.get('language')



