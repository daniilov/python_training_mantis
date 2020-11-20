from model.project import Project
import random
import string


def random_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app, config):
    user_info = config["webadmin"]
    old_projects = app.soap.get_project_list(app.base_url, user_info["username"], user_info["password"])
    project_name = random_name("name_", 10)
    project = Project(name=project_name)
    app.project.add_project(project)
    new_projects = app.soap.get_project_list(app.base_url, user_info["username"], user_info["password"])
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.sorted_name) == sorted(new_projects, key=Project.sorted_name)
