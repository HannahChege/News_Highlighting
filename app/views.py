from flask import render_template
from app  import app

#Views
@app.route('/')
def index():
    '''
    View root page function that return the index page and its data
    '''
    message = 'Hello world'
    return render_template('index.html', message = message)

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


    