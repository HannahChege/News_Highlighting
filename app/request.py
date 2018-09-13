import urllib.request, json
from  .models import Article
from  .models import Source



# Getting api key
api_key = None

# Getting the Article base url
base_url = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
article_url= None
 

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = 'https://newsapi.org/v2/sources?category={}&apiKey={}'

def get_sources(category):

    '''
    Function that gets the json response to our url request
    '''
    source_url = base_url.format( category,api_key)
    with urllib.request.urlopen(source_url) as url:
        source_data = url.read()
        source_response = json.loads(source_data)

        news_results = None

        if source_response['sources']:
            source_results_list = source_response['sources']
            source_news = process_sources(source_results_list)

    return source_news


def process_sources(source_list):
    '''
    Function that processes the source articles and transforn them to a list of Object
    Args:
    source_list: A list of dictionaries that contain source details
    Returns :
    source_news: A list of source objects
    '''
    source_news= []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        source_object = Source(id,name)
        source_news.append(source_object) 
        
    return source_news

def get_articles():
    get_article_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_article_url)
    with urllib.request.urlopen(get_article_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_articles = None

        if get_articles_response['articles']:
            article_articles_list = get_articles_response['articles']
            article_articles = process_articles(article_articles_list)


    return article_articles

def process_articles(articles_list):
    '''
    function that processes the json files of articles from the api key
    '''
    article_articles = []
    for article_item in articles_list:
        source =article_item.get('source.name')
        author = article_item.get('author')
        title= article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get ('publishedAt')
        

        if author:
            article_object = Article(source,author,title,description,url,urlToImage,publishedAt)
            article_articles.append(article_object)


    return article_articles

