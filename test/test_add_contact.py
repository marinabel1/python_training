# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.add_new_contact(Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))
    app.session.logout()


def test_modify_first_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company=u"ООО Тест", mobile="+700000000", work="87210000000"))
    app.session.logout()


def close(app):
    app.destroy()
