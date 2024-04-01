import unittest
from classes.UserRole import UserRole

class TestUserRole(unittest.TestCase):
    def test_validate_role(self):
        # Test pour un rôle valide
        self.assertTrue(UserRole.validate_role(UserRole.GUEST))
        self.assertTrue(UserRole.validate_role(UserRole.USER))
        self.assertTrue(UserRole.validate_role(UserRole.ADMIN))

        # Test pour un rôle invalide
        self.assertFalse(UserRole.validate_role("invalid_role"))
        self.assertFalse(UserRole.validate_role(None))
        self.assertFalse(UserRole.validate_role(123))

    def test_role_str(self):
        # Test pour la description du rôle
        self.assertEqual(UserRole.role_str(UserRole.GUEST), "guest")
        self.assertEqual(UserRole.role_str(UserRole.USER), "user")
        self.assertEqual(UserRole.role_str(UserRole.ADMIN), "admin")

        # Test pour un rôle invalide
        self.assertIsNone(UserRole.role_str("invalid_role"))
        self.assertIsNone(UserRole.role_str(None))
        self.assertIsNone(UserRole.role_str(123))

