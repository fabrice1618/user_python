import sqlite3
import os

class Db:
    """
    Gestionnaire de base de données SQLite3
    """
    DEFAULT_FILE = 'database.db'
    connection = None
    database_file = None

    # Ouverture / fermeture de la base de données
    @classmethod
    def open(cls, database_file=DEFAULT_FILE):
        if cls.is_opened():
            raise RuntimeError("open: database is already opened")
        cls.database_file = database_file
        cls.connection = sqlite3.connect(database_file)

    @classmethod
    def close(cls):
        if not cls.is_opened():
            raise RuntimeError("close: database is not opened")
        cls.connection.close()
        cls.connection = None

    @classmethod
    def is_opened(cls):
        return (cls.connection is not None)

    @classmethod
    def remove(cls, database_file):
        # Suppression de la base de données
        if os.path.exists(database_file):
            os.remove(database_file)

    # retourner un cursor
    @classmethod
    def get_cursor(cls):
        if not cls.is_opened():
            raise RuntimeError("get_cursor: database is not opened")
        return cls.connection.cursor()

    # Execution de requetes
    @classmethod
    def query_insert(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_commit: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        cls.connection.commit()
        return cursor.lastrowid

    @classmethod
    def query_commit(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_commit: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        cls.connection.commit()

    @classmethod
    def query_all(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_all: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    @classmethod
    def query_one(cls, query, data=None):
        if not cls.is_opened():
            raise RuntimeError("query_one: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)        
        result = cursor.fetchone()
        return result

