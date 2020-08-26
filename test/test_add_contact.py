# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.add_new_contact(Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))
    app.session.logout()


def test_delete_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def close(app):
    app.destroy()
