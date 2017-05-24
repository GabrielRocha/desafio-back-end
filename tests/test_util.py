import util


def test_change_single_to_double_quotes():
    assert util.convert_to_double_quotes("'a','p'") == '"a","p"'


def test_flatten_list():
    _list = [1, 2, 3, [3, 4], [1, 2], 0, 9]
    assert util.flatten_list(_list) == [1, 2, 3, 3, 4, 1, 2, 0, 9]


def test_parse_p(tag_p):
    parse = util.parse_p(tag_p)
    assert "type" and "content" in parse
    assert parse['type'] == "text"
    assert parse['content'] == "Texto de exemplo"


def test_parse_img(tag_img):
    parse = util.parse_img(tag_img)
    assert "type" and "content" in parse
    assert parse['type'] == "image"
    assert parse['content'] == "http://s2.glbimg.com/fiat-argo.jpg"


def test_parse_ul(tag_ul):
    parse = util.parse_ul(tag_ul)
    assert "type" and "content" in parse
    assert parse['type'] == "links"
    assert parse['content'] == ["http://null"]


def test_parse_div(tag_div):
    parse = util.parse_div(tag_div)
    assert len(parse) == 2
    assert type(parse) is list
    assert parse[0]['type'] == "links"
    assert parse[0]['content'] == ["http://null"]
    assert parse[1]['type'] == "image"
    assert parse[1]['content'] == "http://s2.glbimg.com/fiat-argo.jpg"


def test_tags_p_method():
    assert util.TAGS['p'] == util.parse_p


def test_tags_img_method():
    assert util.TAGS['img'] == util.parse_img


def test_tags_ul_method():
    assert util.TAGS['ul'] == util.parse_ul


def test_tags_div_method():
    assert util.TAGS['div'] == util.parse_div
