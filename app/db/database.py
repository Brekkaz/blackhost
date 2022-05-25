import os
import psycopg2


class Database(object):

    instance = None

    class __Database:
        _db = None

        def __init__(self):
            self._db = psycopg2.connect(
                host=os.environ["POSTGRES_HOST"],
                database=os.environ["POSTGRES_DB"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
            )

        def getDb(self):
            return self._db

    def __new__(cls):
        if not Database.instance:
            Database.instance = Database.__Database()
        return Database.instance
