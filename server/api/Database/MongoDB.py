
import os

from pymongo import MongoClient


class MongoDB:
    def __init__(self):

        username = "master"
        password = "master1234"
        server = "35.184.61.162"
        self.client = MongoClient(
            'mongodb://%s:%s@%s:27017/iglesiaDB' % (username, password, server))
        self.db = self.client['iglesiaDB']
