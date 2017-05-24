import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_root_tag(feed):
    assert feed.root.name == 'channel'


def test_feed_is_xml(feed):
    assert feed.feed.is_xml


def test_total_items(feed):
    assert len(feed.items) == 2


def test_feed_repr(feed):
    assert feed.__repr__() == "file:///{}/xml/feed.xml".format(BASE_DIR)


def test_valid_json(feed):
    assert json.loads(feed.parse())


def test_parse(feed):
    json_base = json.loads(open(BASE_DIR+"/json").read())
    assert json_base == json.loads(feed.parse())
