class Field:
    def __init__(self, typ=str, default=None, unique=False, required=False):
        self.typ = typ
        self.default=default
        self.required=required
        self.unique=unique

class ForeignKey:
    def __init(self, model, required=False):
        super().__init__(required = required)
        self.model=model
    
    def validate(self, db, value):
        try:
            db.table(self.model).get(value)
        except:
            raise ValueError(f"{self.model} doesnot have a value of {value} in the database.")