from flask import render_template
from app  import app
from .request import get_articles

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting headlines articles
    headlines_articles = get_articles('sports')
    print(headlines_articles)

    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, headlines_articles = headlines_articles)


    