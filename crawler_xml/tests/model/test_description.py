from bs4 import BeautifulSoup
import pytest


@pytest.fixture
def description(item):
    return item.description


def test_text_not_xml(description):
    assert not description.html.is_xml


def test_text_html(description):
    assert isinstance(description.html, BeautifulSoup)


def test_parse(description):
    result = [{"type": "image", "content": "SRC_IMAGE.jpg"},
             {"type": "text", "content": "TEXTO P A STRONG"},
             {"type": "links", "content": ["LINK_LI_1", "LINK_LI_2", "LINK_LI_3"]},
             {"type": "text", "content": "STRONG A TEXTO A"},
             {"type": "text", "content": "TEXTO P A TEXTO A STRONG"}]
    assert description.parse() == result
