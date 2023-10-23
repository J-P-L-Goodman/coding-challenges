import unittest
from unittest.mock import patch
from main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.valid_file_path_step_1 = "tests/step1/valid.json"
        self.invalid_file_path_step_1 = "tests/step1/invalid.json"
        self.valid_file_path_step_2 = "tests/step2/valid.json"
        self.invalid_file_path_step_2 = "tests/step2/invalid.json"
        self.valid2_file_path_step_2 = "tests/step2/valid2.json"
        self.invalid2_file_path_step_2 = "tests/step2/invalid2.json"

    def test_step_1_valid_json(self):
        result = main(self.valid_file_path_step_1)
        self.assertTrue(result)

    def test_step_1_invalid_json(self):
        result = main(self.invalid_file_path_step_1)
        self.assertFalse(result)

    def test_step_2_valid_json(self):
        result = main(self.valid_file_path_step_2)
        self.assertTrue(result)

    def test_step_2_invalid_json(self):
        result = main(self.invalid_file_path_step_2)
        self.assertFalse(result)

    def test_step_2_valid2_json(self):
        result = main(self.valid2_file_path_step_2)
        self.assertTrue(result)

    def test_step_2_invalid2_json(self):
        result = main(self.invalid2_file_path_step_2)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
