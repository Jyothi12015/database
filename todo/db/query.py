from todo.db import Document

class Query:
    """
    A condition for a query. Query can be combination of several conditions
    """
    def __init__(self):
        self._prop = None
        self._test = None

    def __call__(self, doc: Document) -> bool:
        """ 
        Evaluate the query to check if it matches a specific value
        """
        
        if self._prop and self._test:
            return self._test(doc[self._prop])
        return False

    def __getattr__(self, item: str):
        self._prop = item
        return self

    def __getitem__(self, item: str):
        return getattr(self, item)


    def _gen_test(self, func):
        self._test = func
        return self


    def __eq__(self, rhs):
        return self._gen_test(lambda x: x==rhs)
        
    
    def __ne__(self, rhs):
        return self._gen_test(lambda x: x!=rhs)

    def __le__(self, rhs):
        return self._gen_test(lambda x: x<=rhs)

    def __ge__(self, rhs):
        return self._gen_test(lambda x: x>=rhs)

    def __lt__(self, rhs):
        return self._gen_test(lambda x: x<rhs)

    def __gt__(self, rhs):
        return self._gen_test(lambda x: x>rhs)

    def __and__(self, other) -> bool:
        return lambda value: self(value) and other(value)
    
    def __or__(self, other) -> bool:
        return lambda value: self(value) or other(value)

    def __invert__(self) -> bool:
        return lambda value: not self(value)
    
def where(key: str)-> Query:
    return Query()[key]