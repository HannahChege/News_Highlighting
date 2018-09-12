from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources
from ..models import Source,Article



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources= get_sources('general')
    sources= get_sources('sport')
    sources= get_sources('business')
    sources= get_sources('entertainment')
    sources= get_sources('technology')
    
    
   return render_template('index.html', title = title, sources_general = sources_general,sources_sports = sources_sports,sources_entertainment = sources_entertainment,
   sources_business = sources_business,sources_technology = sources_technology)
# @main.route('/articles/<source_id>')
# def articles(source_id):
#     '''
#     View  page function that returns the article1 page and its data
#     '''

#     # Getting sources articles
#     art = get__source(source_id)

#      #title = f'{Article.title}'
#     return render_template('article.html',title =title,name = source_id,art = art)



    