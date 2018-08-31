from app import app
import urllib.request,json
from .models import source
Source = source.Source


#Getting api key
api_key = app.config['SOURCE_API_KEY']

#Getting the source base url
base_url = app.config['SOURCE_API_BASE_URL']

def get_source(category):
    '''
    Function thar gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data =url.read()
        get_source_response = json.loads(get_source_data)

        source_articles = None

        if get_source_response['articles']:
            source_articles_list = get_source_response['articles']
            source_articles = proces_articles(source_articles_list)


    return source_articles

def process_articles(source_list):
    '''
    Function that processes the source articles and transforn them to a list of Object

    Args:
    source_list: A list of dictionaries that contain source details
    Returns :
    source_articles: A list of source objects\
    '''
    source_articles = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        

    return source_articles