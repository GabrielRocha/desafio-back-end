from crawler import CrawlerFeed
from bs4 import BeautifulSoup
import pytest
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session', autouse=True)
def feed():
    ''' Return CrawlerFeed Object with url test'''
    url = "file:///{}/xmls/feed.xml".format(BASE_DIR)
    return CrawlerFeed(url)


@pytest.fixture(scope='session', autouse=True)
def item(feed):
    ''' Return Item'''
    return feed.items[0]


@pytest.fixture
def tag_p():
    return BeautifulSoup("<p>\nTexto de exemplo\n\t\n</p>",
                         "html.parser")


@pytest.fixture
def tag_img():
    html = "<p><img id='221890' src='http://s2.glbimg.com/fiat-argo.jpg'/></p>"
    return BeautifulSoup(html, "html.parser").find('img')


@pytest.fixture
def tag_ul():
    html = "<ul><li><a href='http://null'>1</a></li><li></li></ul>"
    return BeautifulSoup(html, "html.parser")


@pytest.fixture
def tag_div():
    html = "<div><ul><li><a href='http://null'>1</a></li></ul>" \
           "<img id='221890' src='http://s2.glbimg.com/fiat-argo.jpg'/></div>"
    return BeautifulSoup(html, "html.parser").find('div')
