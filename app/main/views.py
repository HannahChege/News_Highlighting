from flask import render_template,request,redirect,url_for
from .import main
from .request import get_articles
from ..request import article_source
from ..models import Source,Article



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting headlines articles
    headlines_general = get_articles('general')
    headlines_sports = get_articles('sports')
    headlines_entertainment = get_articles('entertainment')
    headlines_business = get_articles('business')
    headlines_technology = get_articles('technology')


    title = 'Home - news'
    return render_template('index.html', title = title, headlines_general = headlines_general,headlines_sports = headlines_sports,headlines_entertainment = headlines_entertainment,headlines_business = headlines_business,headlines_technology = headlines_technology)

@main.route('/articles/<id>')
def articles(id):
    '''
    View  page function that returns the article1 page and its data
    '''

    # Getting headlines articles
    art= article_source(id)

    # title = f'{article.title}'
    return render_template('article.html',art = art)



    