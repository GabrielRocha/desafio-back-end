from crawler import CrawlerFeed
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope='session', autouse=True)
def feed():
    ''' Return CrawlerFeed Object with url test'''
    url ="file:///{}/xmls/feed.xml".format(BASE_DIR)
    return CrawlerFeed(url)

@pytest.fixture(scope='session', autouse=True)
def item(feed):
    ''' Return Item'''
    return feed.items[0]