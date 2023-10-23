import unittest
from unittest.mock import patch
from parser_validation import is_valid_json


class TestParserValidation(unittest.TestCase):
    def test_step_1_valid_json(self):
        valid_json = "{}"
        self.assertTrue(is_valid_json(valid_json))

    def test_step_1_invalid_json(self):
        invalid_json = "{"
        self.assertFalse(is_valid_json(invalid_json))

    def test_step_2_valid_json(self):
        valid_json = '{"key":"value"}'
        self.assertTrue(is_valid_json(valid_json))

    def test_step_2_invalid_json_1(self):
        valid_json = '{"key":"value",}'
        self.assertFalse(is_valid_json(valid_json))

    def test_step_2_invalid_json_2(self):
        valid_json = '{"key":}'
        self.assertFalse(is_valid_json(valid_json))

    def test_step_2_invalid_json_3(self):
        valid_json = '{"key": "value",key2: "value"}'
        self.assertFalse(is_valid_json(valid_json))


if __name__ == "__main__":
    unittest.main()
