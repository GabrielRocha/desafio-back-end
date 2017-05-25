from conf.settings_test import CONNECTION
import app as flask_app
import pytest
import json


def login_user(client, user):
    import base64
    # Create User
    client.post("/api/users", data=json.dumps(user),
                content_type='application/json')
    keys = base64.b64encode(bytes(user['username'] + ":"
                                  + user['password'], 'ascii')).decode('ascii')
    return client.open("/api/feed", method="GET",
                       headers={'Authorization': 'Basic {}' + keys})


@pytest.fixture
def app():
    flask_app.User._meta.database = CONNECTION
    flask_app.User.drop_table(fail_silently=True)
    flask_app.User.create_table(fail_silently=True)
    return flask_app.app


@pytest.fixture
def user():
    return dict(username="usuario", password="senha")


def test_get_feed_without_login(client):
    assert client.get("/api/feed").status_code == 401


def test_new_user(client, user):
    assert client.post("/api/users", data=json.dumps(user),
                       content_type='application/json').status_code == 201


def test_total_user(client, user):
    client.post("/api/users", data=json.dumps(user),
                content_type='application/json')
    assert len(flask_app.User.select()) == 1


def test_user_created(client, user):
    client.post("/api/users", data=json.dumps(user),
                content_type='application/json')
    assert len(flask_app.User.select().where(
        flask_app.User.username == "usuario")) == 1


def test_user_unique(client, user):
    client.post("/api/users", data=json.dumps(user),
                content_type='application/json')
    request = client.post("/api/users", data=json.dumps(user),
                          content_type='application/json')
    assert request.status_code == 0
    assert request.json['message'] == "Usuário Já Cadastrado"


def test_username_password_required(client):
    user = dict(username="usuario")
    request = client.post("/api/users", data=json.dumps(user),
                          content_type='application/json')
    assert request.status_code == 0
    assert request.json['message'] == "Username e Password obrigatórios"


def test_get_feed_with_login(client, user):
    request = login_user(client, user)
    assert request.status_code == 200


def test_valid_json_get_feed_with_login(client, user):
    request = login_user(client, user)
    assert json.loads(json.dumps(request.json))


def test_verify_password(client, user):
    client.post("/api/users", data=json.dumps(user),
                content_type='application/json')
    assert flask_app.verify_password(**user)
