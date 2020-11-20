from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self, url, username, password):
        name_projects = []
        client = Client("%s/api/soap/mantisconnect.php?wsdl" % url)
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for element in projects:
                name = element.name
                name_projects.append(Project(name=name))
            return list(name_projects)
        except WebFault:
            return False
