from flask import render_template
from app  import app
from .request import get_articles

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    headlines_articles = get_articles('headlines')
    print(headline_articles)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,headlines = headlines_articles)


    