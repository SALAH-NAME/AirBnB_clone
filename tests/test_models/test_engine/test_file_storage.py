import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        # Test that all returns a dictionary
        self.assertIsInstance(self.storage.all(), dict)
        # Test that the dictionary is empty when no objects have been added
        self.assertEqual(len(self.storage.all()), 8)

    def test_new(self):
        """Test the new method"""
        # Test that new adds an object to the __objects dictionary
        self.storage.new(self.base_model)
        st = "BaseModel.{}"
        self.assertIn(st.format(self.base_model.id), self.storage.all())

    def test_save(self):
        """Test the save method"""
        # Test that save creates a file
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        # Test that reload loads objects from a file
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.base_model.id), objects)

if __name__ == "__main__":
    unittest.main()
