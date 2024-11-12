from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomllib.loads(content)

        Project.name = data['tool']['poetry']['name']
        Project.description = data['tool']['poetry']['description']
        Project.license = data['tool']['poetry']['license']
        Project.authors = data['tool']['poetry']['authors']
        Project.dependencies = data['tool']['poetry']['dependencies']
        Project.dev_dependencies = data['tool']['poetry']['group']['dev']['dependencies']
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(Project.name, Project.description, Project.license, Project.authors,   Project.dependencies, Project.dev_dependencies)
