"""
1.The database must have tables must can be stored in memory(non-persistent) or as JSON files(persistent)
2.Each table must have a name and have a set of documents each identified by an integer id 
3.A document has key value pairs,holding actual data
4.One must be able to insert,delete,update and read documents in a table
5.One must be able to create new table or drop an existing table
6.One must be able to query data from tables based on one more conditions that can be combined using 
 operators and value comparisions as [= / > < ]
 7.Unless specified there must be a default table where any document can be stored 
 
 Nouns:
 Database,memory,tables,document,key,value,data,query,name

 Verbs(Database)
  Create table
  drop table

  verbs (Table)
  insert,delete,update and read documents

  Verbs (Storage)
  reading and writing , new storage

  """
from .table import Table
from .storage import Storage

class DB:
    def __init__(self,storage: Storage):
        """
        intializing a  new database wit appropriate
        """
        self._storage = storage
        self._tables = {}

    def table(self, name):
        """
          Get access to a specific named table.
          returns a table if exits
          creates a new if doesn't exits
        """
        if name in self._tables:
            return _tables[name]

        return Table(name, self._storage)

    def drop(self, name):
        if name in self._tables:
            _tables[name].truncate()
            del _tables[name]

        else:
            raise ValueError(f"No such table {name}")

    def clean(self):
        self._storage.write({})
        self._tables.clear()

