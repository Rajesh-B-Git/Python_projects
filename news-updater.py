# install pip install newsapi-python package

from newsapi import NewsApiClient

# Init
# Add an API_KEY from https://newsapi.org/register
newsapi = NewsApiClient(api_key='API_KEY')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',  # change the q value as per your topic
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# print(top_headlines)
dt = top_headlines['articles']

for x, y in enumerate(dt):
    print(f'{x}{y["description"]}')
