import unittest
from unittest.mock import patch
from parser_validation import is_valid_json


class TestParserValidation(unittest.TestCase):
    def test_simple_valid_json(self):
        valid_json = '{"name": "John", "age": 30}'
        self.assertTrue(is_valid_json(valid_json))

    def test_invalid_json(self):
        invalid_json = "{"
        self.assertFalse(is_valid_json(invalid_json))


if __name__ == "__main__":
    unittest.main()
