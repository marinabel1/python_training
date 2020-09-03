from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))
    app.contact.delete_first_contact()


def test_delete_all_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))
    app.contact.delete_all_contact()
