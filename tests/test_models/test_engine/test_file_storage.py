import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""

    def setUp(self):
        """Set up test cases."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after test cases."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method of the FileStorage class."""
        d = self.storage.all()
        self.assertIsInstance(d, dict)

    def test_new(self):
        """Test the new method of the FileStorage class."""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method of the FileStorage class."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open("file.json", "r") as f:
            content = f.read()
            key = "{}.{}".format(model.__class__.__name__, model.id)
            self.assertIn(key, content)

    def test_reload(self):
        """Test the reload method of the FileStorage class."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        d = self.storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, d)


if __name__ == "__main__":
    unittest.main()
