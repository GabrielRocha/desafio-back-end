from model.item import Item
import pytest


def test_item_title(feed):
    assert Item(feed.items[0]).title == "Fiat Argo é flagrado completamente sem camuflagem"


def test_item_link(feed):
    link = "http://revistaautoesporte.globo.com/Noticias/" \
           "noticia/2017/05/fiat-argo-e-flagrado-completamente-sem-camuflagem.html"
    assert Item(feed.items[0]).link == link


@pytest.mark.skip(reason="Tem que definir o objeto description")
def test_item_description(feed):
    pass