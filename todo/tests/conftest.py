import pytest
from todo.db import JSONStorage
@pytest.fixture
def tempdir():
    return r"C:\Users\jyoth\OneDrive\Desktop\ML clg\project-wek3\todo\temp.db"

@pytest.fixture
def jsonstorage():
    return JSONStorage(r"C:\Users\jyoth\OneDrive\Desktop\ML clg\project-wek3\todo\temp.db")
            