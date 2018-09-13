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
    
    
    title = 'Home - TOP NEWS SOURCES'
    return render_template('index.html', title = title,sources= sources)

# @main.route('/articles/<source_id>')
# def articles(source_id):
#     '''
#     View  page function that returns the article1 page and its data
#     '''

#     # Getting headlines articles
#     art = get__source(source_id)

#      #title = f'{Article.title}'
#     return render_template('article.html',title =title,name = source_id,art = art)



    