import requests
import json
import configparser
from app.elasticsearch import ElasticsearchCore
from app.api_resources import ApiResources
import logging


class Gitlab:

    config = configparser.ConfigParser()
    config.read('config.ini')
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.api_resources = ApiResources()
        self.elasticsearch = ElasticsearchCore(self.api_resources)
        self.gitlab_host = Gitlab.config['gitlab']['host']
        self.projects_endpoint = Gitlab.config['gitlab']['projects_endpoint']
        self.commits_endpoint = Gitlab.config['gitlab']['commits_endpoint']
        self.private_token = Gitlab.config['gitlab']['private_token']

    def do_extraction(self):
        self.extract_projects()
        self.extract_commits()
        self.elasticsearch.index_data()

    def extract_projects(self):
        self.logger.info('Extracting projects from Gitlab...')
        url = self.gitlab_host + self.projects_endpoint
        page = 1
        while True:
            r = requests.get(url, {'page': page}, headers={'PRIVATE-TOKEN': self.private_token}, timeout=15)
            json_projects = json.loads(r.text)

            try:
                json_projects[0]
                self.api_resources.add_projects(json_projects)
                page += 1
            except IndexError:
                break
        self.logger.info('The projects have been extracted')

    def extract_commits(self):
        self.logger.info('Extracting commits from Gitlab...')
        for p in self.api_resources.projects:
            page = 0
            url = self.gitlab_host + '/projects/' + str(p['id']) + self.commits_endpoint

            while True:
                r = requests.get(url, {'page': page}, headers={'PRIVATE-TOKEN': self.private_token}, timeout=15)
                json_commits = json.loads(r.text)

                try:
                    json_commits[0]
                    self.api_resources.add_commits(json_commits, p['name'])
                    page += 1
                except IndexError:
                    break
        self.logger.info('The commits have been extracted')

