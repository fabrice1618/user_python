from classes.Db import Db

Db.open('/data/database.db')

query = """
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('guest', 'admin', 'user'))
    );
"""

Db.query_commit(query)

Db.close()