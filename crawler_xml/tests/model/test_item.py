import ast
import os

from crawler_xml.model.description import Description

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_item_title(item):
    assert item.title == "TITLE"


def test_item_link(item):
    link = "LINK_FEED.html"
    assert item.link == link


def test_item_description(item):
    assert isinstance(item.description, Description)


def test_parse(item):
    with open(BASE_DIR+"/item", "r") as json_file:
        json_item = json_file.read()
    assert item.parse() == ast.literal_eval(json_item)


def test_item_repr(item):
    assert item.__repr__() == "TITLE"
