from app import app
import urllib.request,json
from .models import article
Article = article.Article


#Getting api key
api_key=app.config['NEWS_API_KEY']

#Getting the Article base url
base_url=app.config['NEWS_API_BASE_URL']

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)
    
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
        source_object = Article(id,name,category)
        source_articles.append(source_object)
    return source_articles



def article1(id):
    article1_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article1_url)
    with urllib.request.urlopen(article1_url) as url:
        article1_data = url.read()
        article_response = json.loads(article1_data)

        article1_results = None

        if article1_response['articles']:
            article1_article_list = article1_response['articles']
            article1_results = process_articles1_results(article_article_list)


    return article_source_results
def process_articles1(article_list):
    '''
    Function that processes the article1 articles and transforn them to a list of Object

    Args:
   article1_list: A list of dictionaries that contain sarticle1 details
    Returns :
    article1_articles: A list of article1 objects\
    '''
    article_articles1 = []
    for article1_item in article_list:
        author = article1_item.get('author')
        title = article1_item.get('title')
        description = article1_item.get('description')
        url = article1_item.get('url')
        image = article1_item.get('urlToImage')
        time = article1_item.get('publishedAt')

        article_object = Article(author,title,description,url,image,time)
        article_articles1.append(article_object)
    return article_articles1