from flask import render_template
from app  import app
from .request import get_source
#Views
@app.route('/')
def index():
    '''
    View root page function that return the index page and its data
    '''
    #Getting headlines sources
    headline_source = get_source('source')
    print = 'Headlines'
    title ='Home - NEWS HIGHLIGHTING'
    return render_template('index.html', title = titles,headline = headline_source )

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View source page function that returns the sourcedetails
    '''
    return render_template('source.html,id = source_id')

def index():
    '''
    View root page function that return the index page and its data
    '''
    title = 'NEWS HIGHLIGHTING' 
    return render_template("index.html",title = title)


    