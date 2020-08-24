from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture()
def app():
    fixture = Application()
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Test", header="Train", footer="Testing"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

@pytest.fixture()
def close():
    app.destroy()