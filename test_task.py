import pytest
from task import app as app2


@pytest.fixture()
def app():
    app2.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app2

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_post(client):
    response = client.post("/task",
                           data={
                               "desc": "hello world",
                               "expire": "11/09/2022"
                           })
    assert response.status_code == 201
    data = response.data.decode()
    response = client.get(f"/task/{data.split(' ')[0]}")
    assert b"2022-09-11 hello world" in response.data


def test_post_wrong_date_format(client):
    response = client.post("/task",
                           data={
                               "desc": "hello world",
                               "expire": "11/09/202x2"
                           })
    assert response.status_code == 400


def test_post_no_desc(client):
    response = client.post("/task", data={"expire": "11/09/2022"})
    assert response.status_code == 400


def test_delete(client):
    response = client.post("/task",
                           data={
                               "desc": "hello world",
                               "expire": "11/09/2022"
                           })
    assert response.status_code == 201
    data = response.data.decode()
    response = client.delete(f"/task/{data.split(' ')[0]}")
    assert response.status_code == 204


def test_put(client):
    response = client.post("/task",
                           data={
                               "desc": "hello world",
                               "expire": "11/09/2022"
                           })
    assert response.status_code == 201
    data = response.data.decode()
    response = client.put(f"/task/{data.split(' ')[0]}",
                          data={
                              "desc": "foobar",
                              "expire": "11/09/2023"
                          })
    assert response.status_code == 201
    response = client.get(f"/task/{data.split(' ')[0]}")
    assert b"2023-09-11 foobar" in response.data
