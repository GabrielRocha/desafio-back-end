from peewee import SqliteDatabase
from conf import settings
import re
import pytest


@pytest.mark.parametrize("key", ["URL_FEED",
                                 "CONNECTION"])
def test_key_settings(key):
    assert key in settings.__dict__


@pytest.mark.parametrize("key", ["URL_FEED",
                                 "CONNECTION"])
def test_is_not_none_key(key):
    assert getattr(settings, key)


def test_connection_is_peewee_database():
    assert isinstance(settings.CONNECTION, SqliteDatabase)


def test_url_feed_is_http_link():
    assert re.match(u'^http:\/\/', settings.URL_FEED)
