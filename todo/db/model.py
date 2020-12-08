from .fields import Field, ForeignKey
from todo.dbfactory import DBFactory
from todo.db import where

def Model(klass):
    db=DBFactory.instance()
    klass.table = db.table(klass.__name__)
    klass.properties = [p for p in dir(klass) if isinstance(getattr(klass,p), Field)]

    @classmethod
    def create(cls, *args, **kwargs):
        for prop in klass.properties:
            field = getattr(klass, prop)

            if prop not in kwargs and field.default:
                kwargs[prop] = field.default

            if field.required and prop not in kwargs:
                raise ValueError(f"{prop} is required")

            elif not isinstance(kwargs[prop],field.typ):
                try:
                    kwargs[prop] = field.typ(kwargs[prop])
                except:
                    raise ValueError(f"{prop} must be of type {field.typ}")
            
            if isinstance(field,ForeignKey):
                field.validate(db, kwargs[prop])

            if field.unique and cls.table.search(where(prop)==kwargs[prop]):
                raise ValueError(f"duplicate value found for {prop}:{kwargs[prop]}")

        return cls.table.insert(kwargs)

    @classmethod
    def retrieve(cls,query=None):

        if not query:
            return cls.table.all()
    
        if isinstance(query, Query):
            return cls.table.search(query)
    
        if isinstance(query,int) or query.isnumeric():
            return cls.table.get(query)
    
        raise ValueError("invalid query")

    @classmethod
    def update(cls, *args, **kwargs):
        cls.table.update(*args,**kwargs)

    @classmethod
    def delete(cls, *args, **kwargs):
        cls.table.delete(*args,**kwargs)

    klass.create = create
    klass.retrieve = retrieve
    klass.update = update
    klass.delete = delete
    return klass