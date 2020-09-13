from model.group import Group
from random import randrange


def test_modify_name_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name"))
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    group = Group(name="New group")
    group.id = old_group[index].id
    app.group.modify_group_by_index(group, index)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()
    old_group[index] = group
    assert sorted(old_group, key=Group.id_max) == sorted(new_group, key=Group.id_max)


# def test_modify_header_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(header="Header"))
#     old_group = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_group = app.group.get_group_list()
#     assert len(old_group) == len(new_group)
