import threading


class ApiResources:

    def __init__(self):
        self.projects = []
        self.commits = []

    def add_projects(self, json_projects):
        self.projects.extend(json_projects)

    def add_commits(self, json_commits, project_name):
        t = threading.Thread(target=self.add_project_name, args=(json_commits, project_name,))
        t.start()

        self.commits.extend(json_commits)

    def add_project_name(self, json_commits, project_name):
        for c in json_commits:
            c['project_name'] = project_name
