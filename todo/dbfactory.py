from todo.db import JSONStorage,DB
from .settings import DB_PATH
class DBFactory:
    _instance= None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            storage = JSONStorage(DB_PATH)
            cls._instance = DB(storage)

        return cls._instance