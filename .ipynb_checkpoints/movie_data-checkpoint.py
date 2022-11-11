import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_data():
    
    """
    This function returns the Title of the top 100 movies on imdb and their relative description.
    
    returns:
    
    DataFrame containing 2 columns ('Title','Plot')
    
    """
    
    # Our first url of movies from 0 - 50
    
    url1 = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
    
    # Our second url of movies from 51 - 100
    
    url2 = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt'
    
    urls = [url1, url2]
    
    titles = []

    plots = []

    dict_ = {}
    
    # iterate over urls

    for url in urls:
        
        # Instantiate request

        r = requests.get(url)
        
        # Spice up that beautiful soup
        
        soup = bs(r.content)
        
        # Get all Titles from the page, they have an h3 header and the following class name

        title_page = soup.find_all('h3', {'class':'lister-item-header'})
        
        # Iterate over all the titles

        for title in title_page:
            
            # Append the title to our list
            
            titles.append(title.find_all('a')[0].text)
            
        # Get all descriptions from the page, they have a div tag and the following class name

        divs = soup.find_all('div', {'class':'lister-item mode-advanced'})
        
        # iterate over the descriptions

        for p in divs:
            
            # append
            
            plots.append(p.find_all('p', {'class':'text-muted'})[1].text)
            
        # clean up the descriptions

        plots = [x.replace('\n', '') for x in plots]
        
        # create dictionary

        dict_ = {'Title': [i for i in titles], 'Plot': [i for i in plots]}

    return pd.DataFrame.from_dict(dict_)
