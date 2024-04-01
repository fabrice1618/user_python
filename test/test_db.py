import unittest
from unittest.mock import MagicMock
from classes.Db import Db

class TestDb(unittest.TestCase):

    def setUp(self):
        # Initialisation du mock de la connexion
        self.connection_mock = MagicMock()
        Db.connection = self.connection_mock

    def test_open(self):
        # Test de l'ouverture de la base de données
        Db.open()
        self.assertTrue(Db.connection.connect.called)

    def test_open_already_opened(self):
        # Test de l'ouverture de la base de données lorsqu'elle est déjà ouverte
        Db.connection = MagicMock()
        with self.assertRaises(RuntimeError):
            Db.open()

    def test_close(self):
        # Test de la fermeture de la base de données
        Db.close()
        self.assertTrue(Db.connection.close.called)

    def test_close_not_opened(self):
        # Test de la fermeture de la base de données lorsqu'elle n'est pas ouverte
        Db.connection = None
        with self.assertRaises(RuntimeError):
            Db.close()

    def test_get_cursor(self):
        # Test de l'obtention du curseur
        cursor = Db.get_cursor()
        self.assertTrue(Db.connection.cursor.called)
        self.assertEqual(cursor, Db.connection.cursor.return_value)

    def test_query_insert(self):
        # Test de l'exécution d'une requête d'insertion
        query = "INSERT INTO table (column1, column2) VALUES (?, ?)"
        value1 = 'value1'
        value2 = 'value2'
        data = (value1, value2)
        expected_lastrowid = 123
        cursor_mock = MagicMock()
        cursor_mock.lastrowid = expected_lastrowid
        self.connection_mock.cursor.return_value = cursor_mock

        lastrowid = Db.query_insert(query, data)
        self.assertTrue(self.connection_mock.commit.called)
        self.assertEqual(lastrowid, expected_lastrowid)

    def test_query_commit(self):
        # Test de l'exécution d'une requête de commit
        query = "UPDATE table SET column = ? WHERE id = ?"
        new_value = 'new_value'
        id_value = 123
        data = (new_value, id_value)

        Db.query_commit(query, data)
        self.assertTrue(self.connection_mock.commit.called)

    def test_query_all(self):
        # Test de l'exécution d'une requête retournant plusieurs résultats
        query = "SELECT * FROM table"
        expected_result = [(1, 'value1'), (2, 'value2')]
        cursor_mock = MagicMock()
        cursor_mock.fetchall.return_value = expected_result
        self.connection_mock.cursor.return_value = cursor_mock

        result = Db.query_all(query)
        self.assertEqual(result, expected_result)

    def test_query_one(self):
        # Test de l'exécution d'une requête retournant un seul résultat
        query = "SELECT * FROM table WHERE id = ?"
        id_value = 1
        expected_result = (1, 'value1')
        cursor_mock = MagicMock()
        cursor_mock.fetchone.return_value = expected_result
        self.connection_mock.cursor.return_value = cursor_mock

        result = Db.query_one(query, (id_value,))
        self.assertEqual(result, expected_result)

