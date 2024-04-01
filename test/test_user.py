import unittest
from classes.User import User
from classes.UserRole import UserRole

class TestUser(unittest.TestCase):
    def setUp(self):
        # Initialisation des données de test
        self.valid_id = 1
        self.valid_login = "john_doe"
        self.valid_password = "password123"
        self.valid_role = UserRole.ADMIN
        self.empty_id = 0
        self.empty_login = ""
        self.empty_password = ""

    def test_init(self):
        # Test de l'initialisation de l'utilisateur avec des valeurs valides
        user = User(self.valid_id, self.valid_login, self.valid_password, self.valid_role)
        self.assertEqual(user.id, self.valid_id)
        self.assertEqual(user.login, self.valid_login)
        self.assertTrue(user.verify_password(self.valid_password))
        self.assertEqual(user.role, self.valid_role)

    def test_none(self):
        # Test de l'initialisation de l'utilisateur avec des valeurs None
        user = User()
        self.assertEqual(user.id, None)
        self.assertEqual(user.login, None)
        self.assertEqual(user.pwd_hash, None)
        self.assertEqual(user.role, None)

    def test_invalid_id(self):
        # Test de l'initialisation de l'utilisateur avec un id invalide
        with self.assertRaises(ValueError):
            User("invalid_id", self.valid_login, self.valid_password, self.valid_role)

    def test_invalid_id2(self):
        # Test de l'initialisation de l'utilisateur avec un id invalide
        with self.assertRaises(ValueError):
            User(self.empty_id, self.valid_login, self.valid_password, self.valid_role)

    def test_invalid_login(self):
        # Test de l'initialisation de l'utilisateur avec un login invalide
        with self.assertRaises(ValueError):
            User(self.valid_id, 123, self.valid_password, self.valid_role)

    def test_invalid_login2(self):
        # Test de l'initialisation de l'utilisateur avec un login invalide
        with self.assertRaises(ValueError):
            User(self.valid_id, self.empty_login, self.valid_password, self.valid_role)

    def test_invalid_password(self):
        # Test de l'initialisation de l'utilisateur avec un mot de passe invalide
        with self.assertRaises(ValueError):
            User(self.valid_id, self.valid_login, self.empty_password, self.valid_role)

    def test_invalid_role(self):
        # Test de l'initialisation de l'utilisateur avec un rôle invalide
        with self.assertRaises(ValueError):
            User(self.valid_id, self.valid_login, self.valid_password, "invalid_role")

    def test_valid_repr(self):
        # Test de la représentation sous forme de chaîne de l'utilisateur
        user = User(self.valid_id, self.valid_login, self.valid_password, self.valid_role)
        expected_repr = f"User(id={self.valid_id}, login={self.valid_login}, pwd_hash={user.pwd_hash}, role={UserRole.role_str(self.valid_role)})"
        self.assertEqual(repr(user), expected_repr)

    def test_is_valid(self):
        # Test de la méthode is_valid()
        user = User(self.valid_id, self.valid_login, self.valid_password, self.valid_role)
        self.assertTrue(user.is_valid())

    def test_invalid_is_valid(self):
        # Test de la méthode is_valid() avec des attributs manquants
        user = User(self.valid_id, None, self.valid_password, None)
        self.assertFalse(user.is_valid())
