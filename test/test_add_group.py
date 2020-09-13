from model.group import Group


def test_add_group(app):
    old_group = app.group.get_group_list()
    groups = Group(name="Test", header="Train")
    app.group.create(groups)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(groups)
    assert sorted(old_group, key=Group.id_max) == sorted(new_group, key=Group.id_max)


def test_add_empty_group(app):
    old_group = app.group.get_group_list()
    groups = Group(name="Test", header="Train")
    app.group.create(groups)
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
    old_group.append(groups)
    assert sorted(old_group, key=Group.id_max) == sorted(new_group, key=Group.id_max)

