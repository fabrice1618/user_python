import unittest
import os
from classes.Db import Db
from classes.User import User
from classes.Users import Users

# Chemin vers la base de données de test
TEST_DB_PATH = '/data/test.db'

class TestUsers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Db.open(TEST_DB_PATH)
        # Créer la base de données
        Users.create_table()

    @classmethod
    def tearDownClass(cls):
        # Fermeture de la connexion à la base de données
        Db.close()
        # Supprimer la base de données de test
        cls.delete_test_db()

    @classmethod
    def delete_test_db(cls):
        # Suppression de la base de données de test
        if os.path.exists(TEST_DB_PATH):
            os.remove(TEST_DB_PATH)

    def test_create_user(self):
        # Données de test pour la création d'utilisateur
        user_data = User(id=1, login='test_user', pwd_hash='hashed_password', role='user')
        # Création de l'utilisateur dans la base de données de test
        Users.create(user_data)
        # Vérification si l'utilisateur a été créé avec succès
        user_from_db = Users.read(1)
        self.assertIsNotNone(user_from_db)
        self.assertEqual(user_from_db.login, 'test_user')
        self.assertEqual(user_from_db.pwd_hash, 'hashed_password')
        self.assertEqual(user_from_db.role, 'user')

    def test_read_user(self):
        # Données de test pour la lecture d'utilisateur
        user_data = User(id=1, login='test_user', pwd_hash='hashed_password', role='user')
        Users.create(user_data)
        # Lecture de l'utilisateur depuis la base de données de test
        user_from_db = Users.read(1)
        # Vérification si les données sont correctes
        self.assertIsNotNone(user_from_db)
        self.assertEqual(user_from_db.login, 'test_user')
        self.assertEqual(user_from_db.pwd_hash, 'hashed_password')
        self.assertEqual(user_from_db.role, 'user')

    def test_update_user(self):
        # Données de test pour la mise à jour d'utilisateur
        user_data = User(id=1, login='test_user', pwd_hash='hashed_password', role='user')
        Users.create(user_data)
        # Modification des données de l'utilisateur
        user_data.login = 'updated_user'
        Users.update(user_data)
        # Lecture de l'utilisateur mis à jour depuis la base de données de test
        updated_user_from_db = Users.read(1)
        # Vérification si les données ont été mises à jour correctement
        self.assertEqual(updated_user_from_db.login, 'updated_user')

    def test_delete_user(self):
        # Données de test pour la suppression d'utilisateur
        user_data = User(id=1, login='test_user', pwd_hash='hashed_password', role='user')
        Users.create(user_data)
        # Suppression de l'utilisateur de la base de données de test
        Users.delete(1)
        # Vérification si l'utilisateur a été supprimé avec succès
        deleted_user_from_db = Users.read(1)
        self.assertIsNone(deleted_user_from_db)

    def test_index_users(self):
        # Données de test pour la liste des utilisateurs
        Users.create(User(id=1, login='user1', pwd_hash='pwd1', role='role1'))
        Users.create(User(id=2, login='user2', pwd_hash='pwd2', role='role2'))
        # Liste des utilisateurs depuis la base de données de test
        users = Users.index()
        # Vérification si la liste contient les utilisateurs corrects
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].login, 'user1')
        self.assertEqual(users[1].login, 'user2')

