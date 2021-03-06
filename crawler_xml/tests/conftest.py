from crawler_xml.crawler import CrawlerFeed
from bs4 import BeautifulSoup
import os
import pytest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session', autouse=True)
def feed():
    ''' Return CrawlerFeed Object with url test'''
    url = "file:///{}/xml/feed.xml".format(BASE_DIR)
    return CrawlerFeed(url)


@pytest.fixture(scope='session', autouse=True)
def item(feed):
    ''' Return Item'''
    return feed.items[0]


@pytest.fixture
def html():
    """ Return Basic HTML for test """
    _html = "<p>\nTexto de exemplo\n\t\n</p>" \
            "<div><ul><li><a href='http://null'>1</a></li></ul>" \
            "<img id='221890' src='http://s2.glbimg.com/fiat.jpg'/>" \
            "</div>"
    return BeautifulSoup(_html, "html.parser")
