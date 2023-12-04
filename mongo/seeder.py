from mongos import get_collection
from data import news_data

news = get_collection('feeds', 'news')
print(news)