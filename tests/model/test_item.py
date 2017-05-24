from model.description import Description
import ast
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_item_title(item):
    assert item.title == "TITLE"


def test_item_link(item):
    link = "LINK_FEED.html"
    assert item.link == link


def test_item_description(item):
    assert isinstance(item.description, Description)


def test_parse(item):
    json_item = open(BASE_DIR+"/item", "r").read()
    assert item.parse() == ast.literal_eval(json_item)


def test_item_repr(item):
    assert item.__repr__() == "TITLE"
