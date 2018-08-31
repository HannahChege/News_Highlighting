from flask import render_template
from app  import app
from .request import get_source
#Views
@app.route('/')
def index():
    '''
    View root page function that return the index page and its data
    '''
    #Getting  article sources
    article_sources = get_source('bbc-news')
    print(article_sources)
    title ='Home - NEWS HIGHLIGHTING'
    return render_template('index.html', title = title,bbc_news = article_sources )

# @app.route('/source/<int:source_id>')
# def source(source_id):
#     '''
#     View source page function that returns the sourcedetails
#     '''
#     return render_template('source.html,id = source_id')

# def index():
#     '''
#     View root page function that return the index page and its data
#     '''
#     title = 'NEWS HIGHLIGHTING' 
#     return render_template("index.html",title = title)


    