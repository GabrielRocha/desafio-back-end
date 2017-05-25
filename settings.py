import peewee
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONNECTION = peewee.SqliteDatabase('{}/db/desafio.db'.format(BASE_DIR),
                                   threadlocals=True)

URL_FEED = "http://revistaautoesporte.globo.com/rss/ultimas/feed.xml"
