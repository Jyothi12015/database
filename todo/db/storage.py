from  abc import ABC, abstractmethod
import os
import json
import io


class Storage(ABC):
    @abstractmethod
    def read(self)->dict:
        raise NotImplementedError("To be overriden!")

    @abstractmethod
    def write(self, data: dict)->None:
        raise NotImplementedError("To be overriden!")

    def close(self) -> None:
        pass
class MemoryStorage(Storage):
    """

    Stores the data as JSON in memory
    """
    def __init__(self):
        super().__init__()
        self.memory = {}

    def read(self)->dict:
        return self.memory

    def write(self, data:dict) -> None:
        self.memory = data

class JSONStorage(Storage):

    """
    stores the data as JSON in external file
    """

    def __init__(self, path):
        super().__init__()
        basedir = os.path.dirname(path)
        if not os.path.exists(basedir):
            os.makedirs(basedir)

        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(json.dumps({}))
                f.flush()
        
        self._handle = open(path, 'r+')

    def close(self):
        self._handle.close()

    def read(self)->dict:
        self._handle.seek(0)
        return json.load(self._handle)


    def write(self, data:dict) -> None:
        self._handle.seek(0)
        serialized =json.dumps(data, indent=3)
 
        self._handle.write(serialized)
        self._handle.flush() 
        os.fsync(self._handle.fileno())
        
        self._handle.truncate()
