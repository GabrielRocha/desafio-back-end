from bs4 import BeautifulSoup
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def description(item):
    return item.description


def test_text_not_xml(description):
    assert description.html.is_xml == False

def test_text_html(description):
    assert isinstance(description.html, BeautifulSoup)

def test_total_tag_p(description):
    assert len(description.parse_tag_p()) == 5


@pytest.mark.parametrize("p", open(BASE_DIR+"/description_p", "r").readlines())
def test_description_p(description, p):
    assert p.strip() in description.parse_tag_p()
