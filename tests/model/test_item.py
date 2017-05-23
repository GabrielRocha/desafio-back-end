from model.description import Description
import pytest


@pytest.fixture
def item(feed):
    return feed.items[0]


def test_item_title(item):
    assert item.title == "Fiat Argo é flagrado completamente sem camuflagem"


def test_item_link(item):
    link = "http://revistaautoesporte.globo.com/Noticias/" \
           "noticia/2017/05/fiat-argo-e-flagrado-completamente-sem-camuflagem.html"
    assert item.link == link


def test_item_description(item):
    assert isinstance(item.description, Description)

def test_item_repr(item):
    assert item.__repr__() == "Fiat Argo é flagrado completamente sem camuflagem"