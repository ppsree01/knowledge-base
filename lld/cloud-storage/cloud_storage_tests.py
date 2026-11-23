import unittest
from cloud_storage import CloudStorage

class TestCloudStorage(unittest.TestCase):

    def test_add_file(self):
        storage = CloudStorage()
        result = storage.add_file(name="hello", size=1)
        self.assertEqual(result, True)

        result = storage.add_file(name="hello", size=4)
        self.assertEqual(result, False)

    def test_copy_file(self):
        storage = CloudStorage()
        storage.add_file(name="hello", size=3)
        result = storage.copy_file("hello", "hellow")
        self.assertEqual(result, True)

        result = storage.copy_file("world", "wworld")
        self.assertEqual(result, False)

    def test_get_file_size(self):
        storage = CloudStorage()
        storage.add_file(name="hello", size=3)
        result = storage.get_file_size("hello")
        self.assertEqual(result, 3)
        result = storage.get_file_size("gello")
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()