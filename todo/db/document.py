class Document(dict):
    def __init__(self, id: str, value: dict):
        super().__init__(value)
        self.id = id

    def __getattr__(self, name):
        return self[name]
    
