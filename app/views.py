from flask import render_template
from .request import get_sources, get_source,get_articles
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


   

    title = 'Home - Welcome to The best News Highlight  Website '
    return render_template('index.html', title = title, general=general_news, business=business_news,technology=technology_news,sports=sports_news)

@app.route('/source/<source_name>')
def source(source_name):

    '''
    View news page function that returns the news details page and its data
    '''
    article = get_articles(source_name)
    title = f'{source_name}'

    return render_template('news.html',title = title,articles= article,source=source_name)
