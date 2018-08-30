from app import app
import urllib.request,json
from .models import source
Source = source.Source
#Getting api key
api_key = app.config['ad52b86c9e924d7081cdbc20c6561ff8']
#Getting the source base url
base_url = app.config["https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ad52b86c9e924d7081cdbc20c6561ff8"]

def get_source(category):
    '''
    Function thar gets the json response to our url request
    '''
    get _source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source _url) as url:
        get_source_data =url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_source_response['results']
            source_results = proces_results(source_results_list)


    return source_results

def proces_results(source_list)

