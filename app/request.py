from app import app
import urllib.request, json
from .models import article

Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the Article base url
base_url = app.config['NEWS_API_BASE_URL']


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
        source_object = Article(id, name, category)
        source_articles.append(source_object)
    return source_articles

def article(id):
    article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_url)
    with urllib.request.urlopen(article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_results = None

        if article_response['articles']:
            article_article_list = article_response['articles']
            article_results = process_articles_results(article_article_list)


    return article_results
def process_articles(news):
    '''
    Function that processes the article1 articles and transforn them to a list of Object

    Args:
   article1_list: A list of dictionaries that contain article1 details
    Returns :
    article1_articles: A list of article1 objects\
    '''
    article_results = []
    for article in news:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        time = article.get('publishedAt')


        if url:

            article_objects = Article(author,title,description,url,image,time)
            article_results.append(article_objects)
    return article_results