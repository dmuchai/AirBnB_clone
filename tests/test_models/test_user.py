import unittest
from models.user import User
from models import storage
import os

class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_user_creation(self):
        """Test if the User instance is created correctly"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertIsNotNone(user.id)

    def test_user_save(self):
        """Test if the User instance is saved correctly to the file"""
        user = User()
        user.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_user_all(self):
        """Test if the User instance is correctly added to storage"""
        user = User()
        user.save()
        all_objects = storage.all()
        self.assertIn(f"User.{user.id}", all_objects)

    def test_user_to_dict(self):
        """Test the to_dict method for User"""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())

    def test_user_reload(self):
        """Test the reload method to ensure instances are loaded from the file"""
        user = User()
        user.save()
        user_id = user.id
        storage.reload()
        all_objects = storage.all()
        self.assertIn(f"User.{user_id}", all_objects)
        reloaded_user = all_objects[f"User.{user_id}"]
        self.assertEqual(user.id, reloaded_user.id)

    def run_cmd(self, command):
        """Helper method to run a command in HBNBCommand"""
        from console import HBNBCommand
        console = HBNBCommand()
        console.onecmd(command)


if __name__ == '__main__':
    unittest.main()

