import unittest
from unittest.mock import MagicMock
from classes.Db import Db
from classes.User import User, UserRole
from classes.Users import Users

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.user_data = {'id': 1, 'login': 'test_user', 'password': 'password123', 'role': UserRole.ADMIN}
        self.user = User(**self.user_data)

    def test_create(self):
        with self.assertRaises(ValueError):
            Users.create(None)

        with self.assertRaises(ValueError):
            Users.create(User())

        Db.query_insert = MagicMock(return_value=self.user.id)
        Users.create(self.user)
        self.assertTrue(Db.query_insert.called)
        Db.query_insert.assert_called_once_with(Users.SQL_CREATE, (self.user.login, self.user.pwd_hash, self.user.role.value))
        self.assertIsNotNone(self.user.id)

    def test_read(self):
        with self.assertRaises(ValueError):
            Users.read(None)

        Db.query_one = MagicMock(return_value=tuple(self.user_data.values()))
        result = Users.read(self.user.id)
        self.assertTrue(Db.query_one.called)
        Db.query_one.assert_called_once_with(Users.SQL_READ, (self.user.id,))
        self.assertIsInstance(result, User)
        self.assertEqual(result.id, self.user.id)
        self.assertEqual(result.login, self.user.login)
        self.assertEqual(result.pwd_hash, self.user.pwd_hash)
        self.assertEqual(result.role, self.user.role)

    def test_update(self):
        with self.assertRaises(ValueError):
            Users.update(None)

        with self.assertRaises(ValueError):
            Users.update(User())

        Users.update(self.user)
        self.assertTrue(Db.query_commit.called)
        Db.query_commit.assert_called_once_with(Users.SQL_UPDATE, (self.user.login, self.user.pwd_hash, self.user.role.value, self.user.id))

    def test_delete(self):
        with self.assertRaises(ValueError):
            Users.delete(None)

        Users.delete(self.user.id)
        self.assertTrue(Db.query_commit.called)
        Db.query_commit.assert_called_once_with(Users.SQL_DELETE, (self.user.id,))

    def test_index(self):
        Db.query_all = MagicMock(return_value=[tuple(self.user_data.values())])
        result = Users.index()
        self.assertTrue(Db.query_all.called)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], User)
        self.assertEqual(result[0].id, self.user.id)
        self.assertEqual(result[0].login, self.user.login)
        self.assertEqual(result[0].pwd_hash, self.user.pwd_hash)
        self.assertEqual(result[0].role, self.user.role)

    def test_index_generator(self):
        Db.query_all = MagicMock(return_value=[tuple(self.user_data.values())])
        generator = Users.index_generator()
        self.assertTrue(Db.query_all.called)
        self.assertIsNotNone(generator)
        user = next(generator)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, self.user.id)
        self.assertEqual(user.login, self.user.login)
        self.assertEqual(user.pwd_hash, self.user.pwd_hash)
        self.assertEqual(user.role, self.user.role)

    def test_find_login(self):
        with self.assertRaises(ValueError):
            Users.find_login(None)

        Db.query_one = MagicMock(return_value=(self.user.id,))
        result = Users.find_login(self.user.login)
        self.assertTrue(Db.query_one.called)
        Db.query_one.assert_called_once_with(Users.SQL_FIND_LOGIN, (self.user.login,))
        self.assertEqual(result, self.user.id)

    def test_exist(self):
        with self.assertRaises(ValueError):
            Users.exist(None)

        Db.query_one = MagicMock(return_value=(1,))
        result = Users.exist(self.user.id)
        self.assertTrue(Db.query_one.called)
        Db.query_one.assert_called_once_with(Users.SQL_EXIST, (self.user.id,))
        self.assertTrue(result)

