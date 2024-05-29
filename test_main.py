import os
import unittest
from main import save_user_data

class TestSaveUserData(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_user_data.txt'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_user_data(self):
        save_user_data("John Doe", 30, self.test_file)
        with open(self.test_file, 'r') as file:
            content = file.read()
        self.assertIn("Name: John Doe, Age: 30", content)

if __name__ == '__main__':
    unittest.main()
