import unittest
from classes.Db import Db
from classes.User import User
from classes.UserRole import UserRole
from classes.Users import Users
from classes.password import hash_password

# Chemin vers la base de données de test
TEST_DB_PATH = '/data/test.db'

def new_test_database():
    Db.remove(TEST_DB_PATH)
    Db.open(TEST_DB_PATH)
    # Créer la base de données
    Users.create_table()

def remove_test_database():
    Db.close()
    # Supprimer la base de données de test
    Db.remove(TEST_DB_PATH)

class TestUsers(unittest.TestCase):
    #@classmethod
    #def setUpClass(cls):
    #    Db.remove(TEST_DB_PATH)
    #    Db.open(TEST_DB_PATH)
    #    # Créer la base de données
    #    Users.create_table()

    def setUp(self):
        # Initialisation des données de test
        self.valid_user = 'test_user'
        self.valid_role = UserRole.USER
        self.valid_pwd_hash = hash_password('password1234')
        self.updated_user = 'updated_user'
        self.user1_login = 'user1'
        self.user1_pwd_hash = hash_password('pwd1')
        self.user1_role = UserRole.USER
        self.user2_login = 'user2'
        self.user2_pwd_hash = hash_password('pwd2')
        self.user2_role = UserRole.ADMIN

    #@classmethod
    #def tearDownClass(cls):
    #    # Fermeture de la connexion à la base de données
    #    Db.close()
    #    # Supprimer la base de données de test
    #    Db.remove(TEST_DB_PATH)

    def test_create_user(self):
        new_test_database()
        # Données de test pour la création d'utilisateur
        user_data = User(id=1, login=self.valid_user, pwd_hash=self.valid_pwd_hash, role=self.valid_role)
        # Création de l'utilisateur dans la base de données de test
        Users.create(user_data)
        # Vérification si l'utilisateur a été créé avec succès
        user_from_db = Users.read(1)
        self.assertIsNotNone(user_from_db)
        self.assertEqual(user_from_db.login, self.valid_user)
        self.assertEqual(user_from_db.pwd_hash, self.valid_pwd_hash)
        self.assertEqual(user_from_db.role, self.valid_role)
        remove_test_database()

    def test_read_user(self):
        new_test_database()
        # Données de test pour la lecture d'utilisateur
        user_data = User(id=1, login=self.valid_user, pwd_hash=self.valid_pwd_hash, role=self.valid_role)
        Users.create(user_data)
        # Lecture de l'utilisateur depuis la base de données de test
        user_from_db = Users.read(1)
        # Vérification si les données sont correctes
        self.assertIsNotNone(user_from_db)
        self.assertEqual(user_from_db.login, self.valid_user)
        self.assertEqual(user_from_db.pwd_hash, self.valid_pwd_hash)
        self.assertEqual(user_from_db.role, self.valid_role)
        remove_test_database()

    def test_update_user(self):
        new_test_database()
        # Données de test pour la mise à jour d'utilisateur
        user_data = User(id=1, login=self.valid_user, pwd_hash=self.valid_pwd_hash, role=self.valid_role)
        Users.create(user_data)
        # Modification des données de l'utilisateur
        user_data.login = self.updated_user
        Users.update(user_data)
        # Lecture de l'utilisateur mis à jour depuis la base de données de test
        updated_user_from_db = Users.read(1)
        # Vérification si les données ont été mises à jour correctement
        self.assertEqual(updated_user_from_db.login, self.updated_user)
        remove_test_database()

    def test_delete_user(self):
        new_test_database()
        # Données de test pour la suppression d'utilisateur
        user_data = User(id=1, login=self.valid_user, pwd_hash=self.valid_pwd_hash, role=self.valid_role)
        Users.create(user_data)
        # Suppression de l'utilisateur de la base de données de test
        Users.delete(1)
        # Vérification si l'utilisateur a été supprimé avec succès
        deleted_user_from_db = Users.read(1)
        self.assertIsNone(deleted_user_from_db)
        remove_test_database()

    def test_index_users(self):
        new_test_database()
        # Données de test pour la liste des utilisateurs
        Users.create(User(id=1, login=self.user1_login, pwd_hash=self.user1_pwd_hash, role=self.user1_role))
        Users.create(User(id=2, login=self.user2_login, pwd_hash=self.user2_pwd_hash, role=self.user2_role))
        # Liste des utilisateurs depuis la base de données de test
        users = Users.index()
        # Vérification si la liste contient les utilisateurs corrects
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].login, self.user1_login)
        self.assertEqual(users[1].login, self.user2_login)
        remove_test_database()

