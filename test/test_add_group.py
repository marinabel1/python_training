from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Test", header="Train"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


def close(app):
    app.destroy()