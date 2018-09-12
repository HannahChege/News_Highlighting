import urllib.request, json
from  .models import Article
from  .models import Source



# Getting api key
api_key = None

# Getting the Article base url
base_url = None
article_url= None
 

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources():

    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(, api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['sources']:
            article_results_list = get_articles_response['sources']
            article_results = process_sources(article_results_list)

    return article_results


def process_sources(source_list):
    '''
    Function that processes the source articles and transforn them to a list of Object
    Args:
    source_list: A list of dictionaries that contain source details
    Returns :
    source_articles: A list of source objects
    '''
    source_articles = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        category = source_item.get('category')
        if id:
            source_object = Source(id,name,category)
            source_articles.append(source_object)
    return source_articles

def get_article_source(id):
    get_article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(get_article_source_url)
    with urllib.request.urlopen(get_article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(my_articles):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in my_articles:
        author = article.get('author')
        title= article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get(' urlToImage')
        publishedAt = article.get ('publishedAt')
        

        if urlToImage:
            article_objects = Article(author,title,description,url,urlToImage,publishedAt)
            article_source_results.append(article_objects)
    return article_source_results

