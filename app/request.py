from app import app
import urllib.request, json
from  .models import article
# from  .models import source

Article = article.Article
Source = article.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the Article base url
base_url = app.config['NEWS_API_BASE_URL']
article_url= app.config['ARTICLE_API_URL']

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['sources']:
            article_results_list = get_articles_response['sources']
            article_results = process_articles(article_results_list)

    return article_results


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
        category = source_item.get('category')
        description = source_item.get('description')
        url = source_item.get('url')
        source_object = Article(id, name, category)
        source_articles.append(source_object)
    return source_articles

def article_source():
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(article1_list):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    while(len(source_results) <= 10):
        for article in news:
            source = article.get('source')
            author = article.get('author')
            title= article.get('title')
            description = article.get('description')
            url = article.get('url')
            image = article.get(' urlToImage')
            time = article.get ('publishedAt')
        

        if url:
            article_objects = Article(source,author,title,description,url,image,time)
            article_source_results.append(article_objects)

    return article_source_results

