from passlib.apps import custom_app_context as password_context
from conf.settings import CONNECTION
import peewee


class User(peewee.Model):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()

    def set_password(self, password):
        self.password = password_context.hash(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password)

    class Meta:
        database = CONNECTION
