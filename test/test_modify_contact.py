from model.contact import Contact


def test_modify_first_contact(app):
    contact = Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November", "1997")
    if app.contact.count() == 0:
        app.contact.add_new_contact(contact)
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(Contact(company=u"ООО Тест", mobile="+700000000", work="87210000000"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)
