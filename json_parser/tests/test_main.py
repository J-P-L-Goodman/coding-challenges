import unittest
from unittest.mock import patch
from main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.valid_file_path = "tests/step1/valid.json"
        self.invalid_file_path = "tests/step1/invalid.json"

    def test_simple_valid_json(self):
        result = main(self.valid_file_path)
        self.assertTrue(result)

    def test_simple_invalid_json(self):
        result = main(self.invalid_file_path)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
