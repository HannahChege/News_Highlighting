from flask import render_template
from app  import app
from .request import get_articles,get_article1

@app.route('/')
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

@app.route('/article1/<int:id>')
def article1(id):
    '''
    View  page function that returns the article1 page and its data
    '''

    # Getting headlines articles
    article1= get_article1('id')
    # print(article1)

    title = f'{article1.title}'
    return render_template('article.html',title= title ,article1 = article1)

@app.route('/category/<cat_name>')
def category(cat_name):
    '''
    function that returns the category page and its data
    '''

    # Getting headlines articles
    category= get_category('cat_name')
    print(category)

    title = f'{cat_name}'
    return render_template('category.html',name= category ,title = title)



    