from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))
    app.contact.modify_first_contact(Contact(company=u"ООО Тест", mobile="+700000000", work="87210000000"))
