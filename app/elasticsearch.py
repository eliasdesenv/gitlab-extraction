import configparser
from elasticsearch import Elasticsearch
import threading
import logging


class ElasticsearchCore:
    config = configparser.ConfigParser()
    config.read('config.ini')
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    def __init__(self, api_resources):
        self.es = Elasticsearch(hosts=ElasticsearchCore.config['elasticsearch']['host'])
        self.api_resources = api_resources

    def index_data(self):
        threading.Thread(target=self.index_projects).start()
        threading.Thread(target=self.index_commits).start()

    def index_projects(self):
        self.logger.info('Indexing projects in Elasticsearch...')
        for project in self.api_resources.projects:
            self.es.index(index="gitlab-projects", doc_type="doc", body=project)
        self.logger.info('The projects have been indexed')

    def index_commits(self):
        self.logger.info('Indexing commits in Elasticsearch...')
        for commit in self.api_resources.commits:
            self.es.index(index="gitlab-commits", doc_type="doc", body=commit)
        self.logger.info('The commits have been indexed')
