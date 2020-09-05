# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new_contact(Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))

