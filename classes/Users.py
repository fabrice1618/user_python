from classes.Db import Db
from classes.User import User

class Users:
    """
    Classe Users
    """
    SQL_CREATE = '''
        INSERT INTO users (login, password_hash, role) 
        VALUES (?, ?, ?)
        '''
    SQL_READ = "SELECT * FROM users WHERE id = ?"
    SQL_UPDATE = '''UPDATE users 
        SET login = ?, password_hash = ?, role = ? 
        WHERE id = ?'''
    SQL_DELETE = "DELETE FROM users WHERE id = ?"
    SQL_INDEX = "SELECT * FROM users"
    SQL_FIND_LOGIN = "SELECT id FROM users WHERE login = ?"
    SQL_EXIST = "SELECT COUNT(*) FROM users WHERE id = ?"

    @classmethod
    def create(cls, user):
        if not User.is_valid(user):
            raise ValueError("Users.create: user not valid")            
        id = Db.query_insert(cls.SQL_CREATE, (user.login, user.pwd_hash, user.role.value))
        user.id = id

    @classmethod
    def read(cls, id):
        if id is None or not User.validate_id(id):
            raise ValueError("Users.read: id invalide")
        result = Db.query_one(cls.SQL_READ, (id,))
        return User.from_tuple(result)

    @classmethod
    def update(cls, user):
        if user is None or not User.is_valid(user):
            raise ValueError("Users.update: user invalide")
        Db.query_commit(cls.SQL_UPDATE, (user.login, user.pwd_hash, user.role.value, user.id))

    @classmethod
    def delete(cls, id):
        if id is None or not User.validate_id(id):
            raise ValueError("Users.delete: id invalide")
        Db.query_commit(cls.SQL_DELETE, (id,))

    @classmethod
    def index(cls):
        result = Db.query_all(cls.SQL_INDEX)
        if result is None:
            return list()
        users = [User.from_tuple(data) for data in result]
        return users

    @classmethod
    def index_generator(cls):
        result = Db.query_all(cls.SQL_INDEX)
        if result is None:
            return
        for data in result:
            yield User.from_tuple(data)
        return

    @classmethod
    def find_login(cls, login):
        if login is None or not User.validate_login(login):
            raise ValueError("Users.find_login: login invalide")
        result = Db.query_one(cls.SQL_FIND_LOGIN, (login,))
        if result is None:
            return None
        else:
            return result[0]

    @classmethod
    def exist(cls, id):
        if id is None or not User.validate_id(id):
            raise ValueError("Users.exist: id invalide")
        result = Db.query_one(cls.SQL_EXIST, (id,))
        return (result[0] > 0)
