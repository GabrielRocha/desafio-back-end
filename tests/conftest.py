from crawler import CrawlerFeed
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope='session', autouse=True)
def feed():
    ''' Return CrawlerFeed Object with url test'''
    url = BASE_DIR + "/xmls/feed.xml"
    return CrawlerFeed(url)
