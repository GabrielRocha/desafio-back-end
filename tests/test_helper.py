from helper import change_single_to_double_quotes


def test_change_single_to_double_quotes():
    assert change_single_to_double_quotes("'a','p'") == '"a","p"'
