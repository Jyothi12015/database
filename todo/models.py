from todo.db import Model, Field, ForeignKey, where
import hashlib, uuid
@Model
class User:
    salt = Field(required=True)
    username = Field(required=True, unique=True)
    name = Field(required=True)
    password = Field(required=True)

    @classmethod
    def hashpwd(cls, password, salt):
        sha = hashlib.sha256()
        to_hash = str(password) + str(salt)
        sha.update(to_hash.encode())
        return sha.hexdigest()

    @classmethod
    def register(cls, name, username, password):
        if name==None:
            raise ValueError("Name is required")
        sha = uuid.uuid4().hex
        password=cls.hashpwd(password, salt)
        return cls.create(name=name, salt=salt, username=username, password=password)

    @classmethod
    def validate(cls, username, password):
        user = cls.retrieve(where('username')==username)

        if len(user)==0:
            raise ValueError("No such user")
        else:
            u = user[0]
            salt = u.salt
            password = cls.hashpwd(password,salt)
            if u.password != password:
                raise ValueError("Incorrect password")
            return u

@Model
class Todo:
    task = Field(required=True)
    created = Field(typ=int, required=True)
    due = Field(typ=int, required=True)
    priority = Field(typ=int, default=0)
    archived = Field(typ=bool, default=False)
    done = Field(typ=bool, default=False)
    userid = Field(typ=int, required=True)

@Model
class Session:
    sessionid = Field(required=True)
    userid = Field(typ=int, required=True)
    name = Field(required=True)
    state  = Field(typ=dict, default={})
