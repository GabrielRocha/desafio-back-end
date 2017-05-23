import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_root_tag(feed):
    assert feed.root.name == 'channel'


def test_total_items(feed):
    assert len(feed.items) == 12

def test_feed_repr(feed):
    assert feed.__repr__() == "file:////home/tests/xmls/feed.xml"

@pytest.mark.skip(reason="Tem que definir o objeto description")
@pytest.mark.parametrize("item", open(BASE_DIR+"/items", "r").readlines())
def test_parse_items(feed, item):
    assert item.replace("\n", "") in feed.parse_items()
