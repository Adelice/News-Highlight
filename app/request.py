from app import app
import urllib.request,json
from .models import source
from .models import article
Source = source.Source
Article = article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']
base_url = app.config["SOURCE_API_BASE_URL"]
base_url1= app.config["ARTICLE_API_BASE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_sources = None


        if get_sources_response['sources']:
            source_sources_list = get_sources_response['sources']
            source_sources = process_sources(source_sources_list)


    return source_sources
def process_sources(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_sources = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category= source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_sources.append(source_object)

    return source_sources
def get_source(id):
    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id= source_details_response.get('id')
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url = source_details_response.get('url')
            category = source_details_response.get('category')
            language = source_details_response.get('language')
            country = source_details_response.get('country')

            source_object = Source(id,name,description,url,category,language,country)

    return source_object
def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url1.format(source,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results= None


        if get_articles_response['articles']:
           article_results_list = get_articles_response['articles']
           article_results = process_articles(article_results_list)


    return article_results
def process_articles(article_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
       article_results: A list of article objects
    '''
    article_results=[]
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage= article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
           article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
           article_results.append(article_object)

    return article_results