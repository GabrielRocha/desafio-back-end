from model.description import Description


def test_item_title(item):
    assert item.title == "TITLE"


def test_item_link(item):
    link = "LINK_FEED.html"
    assert item.link == link


def test_item_description(item):
    assert isinstance(item.description, Description)


def test_item_repr(item):
    assert item.__repr__() == "TITLE"
