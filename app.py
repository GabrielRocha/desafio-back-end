from flask_httpauth import HTTPBasicAuth
from peewee import IntegrityError
from conf.settings import URL_FEED
from crawler_xml.crawler import CrawlerFeed
from model import User
import flask

app = flask.Flask(__name__)
auth = HTTPBasicAuth()
User.create_table(fail_silently=True)


@auth.verify_password
def verify_password(username, password):
    user = User.select().where(User.username == username).first()
    if not user or not user.verify_password(password):
        return False
    flask.g.user = user
    return True


@app.errorhandler(400)
def custom400(error):
    response = flask.jsonify({'message': error.description})
    response.status_code = 400
    response.status = 'error.Bad Request'
    return response


@app.route('/api/users', methods=['POST'])
def new_user():
    username = flask.request.json.get('username')
    password = flask.request.json.get('password')
    if username is None or password is None:
        flask.abort(400, "Username e Password obrigatórios")
    try:
        user = User(username=username)
        user.set_password(password)
        user.save()
    except IntegrityError:
        flask.abort(400, "Usuário Já Cadastrado")
    return flask.jsonify({'username': username}), 201


@app.route('/api/feed')
@auth.login_required
def get_resource():
    json_string = CrawlerFeed(URL_FEED).parse()
    response = flask.Response(json_string,
                              content_type="application/json; charset=utf-8")
    return response
