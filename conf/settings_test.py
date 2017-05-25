from .settings import BASE_DIR
from peewee import SqliteDatabase

CONNECTION = SqliteDatabase('{}/db/test.db'.format(BASE_DIR),
                            threadlocals=True)
