from model import User
import peewee
import pytest
import re


@pytest.fixture
def user():
    """ User model """
    return User()


def test_user_has_username():
    assert getattr(User, "username")


@pytest.mark.parametrize("field", ["username",
                                   "password"])
def test_field_is_peewee_charfield(field):
    assert isinstance(getattr(User, field), peewee.CharField)


def test_username_is_unique():
    assert User.username.unique


def test_user_has_password():
    assert getattr(User, "password")


def test_verify_password(user):
    user.set_password("teste")
    assert user.verify_password("teste")
    assert not(user.verify_password("error"))


def test_set_password(user):
    user.set_password("teste")
    assert re.match("^\$6\$rounds", user.password)
