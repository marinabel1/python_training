from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(company=u"ООО Тест", mobile="+700000000", work="87210000000"))
