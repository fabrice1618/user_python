import sqlite3

class Db:
    """
    Gestionnaire de base de données SQLite3
    """
    DEFAULT_FILE = 'database.db'
    connection = None

    # Ouverture / fermeture de la base de données
    @classmethod
    def open(cls, database_file=DEFAULT_FILE):
        if cls.connection is not None:
            raise RuntimeError("open: database is already opened")
        cls.connection = sqlite3.connect(database_file)

    @classmethod
    def close(cls):
        if cls.connection is None:
            raise RuntimeError("close: database is not opened")
        cls.connection.close()
        cls.connection = None

    # retourner un cursor
    @classmethod
    def get_cursor(cls):
        if cls.connection is None:
            raise RuntimeError("get_cursor: database is not opened")
        return cls.connection.cursor()

    # Execution de requetes
    @classmethod
    def query_insert(cls, query, data=None):
        if cls.connection is None:
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
        if cls.connection is None:
            raise RuntimeError("query_commit: database is not opened")
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        cls.connection.commit()

    @classmethod
    def query_all(cls, query, data=None):
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    @classmethod
    def query_one(cls, query, data=None):
        cursor = cls.connection.cursor()
        if data is None:
            cursor.execute(query)
        else:
            cursor.execute(query, data)        
        result = cursor.fetchone()
        return result

