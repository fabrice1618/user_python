import unittest
from test_user import TestUser
from test_user_role import TestUserRole
from test_db import TestDb
from test_users import TestUsers

if __name__ == '__main__':
    # Créer une suite de tests pour UserRole
    suite_user_role = unittest.TestLoader().loadTestsFromTestCase(TestUserRole)
    
    # Créer une suite de tests pour User
    suite_user = unittest.TestLoader().loadTestsFromTestCase(TestUser)

    # Créer une suite de tests pour Db
    suite_db = unittest.TestLoader().loadTestsFromTestCase(TestDb)

    # Créer une suite de tests pour Users
    suite_users = unittest.TestLoader().loadTestsFromTestCase(TestUsers)

    # Créer une suite de tests globale et ajouter les suites de tests individuelles
    all_tests = unittest.TestSuite()
    all_tests.addTests(suite_user_role)
    all_tests.addTests(suite_user)
    all_tests.addTests(suite_db)
    all_tests.addTests(suite_users)

    # Exécuter la suite de tests globale
    runner = unittest.TextTestRunner()
    runner.run(all_tests)
