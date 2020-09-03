from model.group import Group


def test_modify_name_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_header_group(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Header"))
    app.group.modify_first_group(Group(header="New header"))
