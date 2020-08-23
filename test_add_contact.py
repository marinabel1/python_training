# -*- coding: utf-8 -*-
from fixture.application import Application
from contact import Contact
import pytest


@pytest.fixture()
def app():
    fixture = Application()
    return fixture

def test_add_contact(app):
    app.login( username="admin", password="secret")
    app.add_new_contact(Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))
    app.logout()

@pytest.fixture()
def close():
    app.destroy()
