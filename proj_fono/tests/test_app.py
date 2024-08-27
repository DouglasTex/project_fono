from http import HTTPStatus

from fastapi.testclient import TestClient

from proj_fono.app import app

client = TestClient(app)


def test_read_root_return_ok_and_message():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'aoba caralho'}
