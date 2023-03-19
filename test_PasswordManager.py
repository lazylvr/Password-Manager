import unittest
from password_manager import PasswordManager

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        self.password_manager = PasswordManager(':memory:')

    def tearDown(self):
        self.password_manager.close()

    def test_add_password(self):
        self.password_manager.add_password('google.com', 'john_doe', 'password123')
        self.assertEqual(self.password_manager.get_password('google.com', 'john_doe'), 'password123')

    def test_update_password(self):
        self.password_manager.add_password('facebook.com', 'jane_doe', 'oldpassword')
        self.password_manager.update_password('facebook.com', 'jane_doe', 'newpassword')
        self.assertEqual(self.password_manager.get_password('facebook.com', 'jane_doe'), 'newpassword')

    def test_delete_password(self):
        self.password_manager.add_password('linkedin.com', 'john_smith', 'password123')
        self.password_manager.delete_password('linkedin.com', 'john_smith')
        self.assertIsNone(self.password_manager.get_password('linkedin.com', 'john_smith'))

if __name__ == '__main__':
    unittest.main()
