import unittest
from lexer import tokenize


class TestLexer(unittest.TestCase):
    def test_step_1_valid_json(self):
        json_str = "{}"
        tokens = tokenize(json_str)
        self.assertEqual(tokens, [(8, "{"), (9, "}")])

    def test_step_1_invalid_json(self):
        invalid_json_str = ""
        tokens = tokenize(invalid_json_str)
        self.assertEqual(tokens, [])

    def test_step_2_valid_json(self):
        json_str = '{"key": "value"}'
        tokens = tokenize(json_str)
        self.assertEqual(
            tokens, [(8, "{"), (1, "key"), (6, ":"), (1, "value"), (9, "}")]
        )

    def test_step_2_invalid_json(self):
        json_str = '{"key": "value",}'
        tokens = tokenize(json_str)
        self.assertEqual(
            tokens, [(8, "{"), (1, "key"), (6, ":"), (1, "value"), (7, ","), (9, "}")]
        )


if __name__ == "__main__":
    unittest.main()
