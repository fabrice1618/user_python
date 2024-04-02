import unittest
#import sqlite3
import os
from classes.Db import Db

# Chemin vers la base de données de test
TEST_DB_PATH = '/data/test.db'

class TestDb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Créer la base de données de test
        cls.create_test_db()

    @classmethod
    def tearDownClass(cls):
        # Supprimer la base de données de test
        cls.delete_test_db()

    @classmethod
    def create_test_db(cls):
        # Connexion à la base de données de test
        Db.open(TEST_DB_PATH)
        # Création d'une table de test
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS test_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
            '''
        Db.query_commit(create_table_query)

    @classmethod
    def delete_test_db(cls):
        # Fermeture de la connexion à la base de données
        Db.close()
        # Suppression de la base de données de test
        if os.path.exists(TEST_DB_PATH):
            os.remove(TEST_DB_PATH)

    def test_query_insert(self):
        # Données de test
        name = 'John Doe'
        # Exécution de la requête INSERT
        row_id = Db.query_insert('INSERT INTO test_table (name) VALUES (?)', (name,))
        # Vérification du résultat
        self.assertIsInstance(row_id, int)
        self.assertGreater(row_id, 0)

    def test_query_commit(self):
        # Données de test
        name = 'Jane Doe'
        # Exécution de la requête INSERT
        Db.query_insert('INSERT INTO test_table (name) VALUES (?)', (name,))
        # Exécution de la requête COMMIT
        #Db.query_commit('COMMIT')
        # Récupération des données insérées
        result = Db.query_one('SELECT * FROM test_table WHERE name = ?', (name,))
        # Vérification du résultat
        self.assertIsNotNone(result)

    def test_query_all(self):
        # Exécution de la requête SELECT
        result = Db.query_all('SELECT * FROM test_table')
        # Vérification du résultat
        self.assertIsInstance(result, list)

    def test_query_one(self):
        # Données de test
        name = 'John Doe'
        # Exécution de la requête SELECT
        result = Db.query_one('SELECT * FROM test_table WHERE name = ?', (name,))
        # Vérification du résultat
        self.assertIsNotNone(result)
        self.assertEqual(result[1], name)

