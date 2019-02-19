from flask import render_template
from .request import get_sources, get_source
from app import app
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    technology_news= get_sources('technology')
    sports_news=get_sources('sports')


   

    title = 'Home - Welcome to The best News Highlight Review Website Online'
    return render_template('index.html', title = title, general=general_news, business=business_news,technology=technology_news,sports=sports_news)
@app.route('/source/<id>')
def source(id):

    '''
    View news page function that returns the news details page and its data
    '''
    source = get_source(id)
    name = f'{source.name}'

    return render_template('news.html',name = name,source=source)
