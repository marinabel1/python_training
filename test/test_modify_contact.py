from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    contact = Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November", "1997")
    if app.contact.count() == 0:
        app.contact.add_new_contact(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(Contact(company=u"ООО Тест", mobile="+700000000", work="87210000000"), index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)
