import unittest
from lexer import tokenize


class TestLexer(unittest.TestCase):
    def test_simple_valid_json(self):
        json_str = "{}"
        tokens = tokenize(json_str)
        self.assertEqual(tokens, [(8, "{"), (9, "}")])

    def test_invalid_json(self):
        invalid_json_str = ""
        tokens = tokenize(invalid_json_str)
        self.assertEqual(tokens, [])


if __name__ == "__main__":
    unittest.main()
