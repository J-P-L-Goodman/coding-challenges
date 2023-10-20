import unittest
from io import StringIO
from unittest.mock import patch
from ccwc import (
    count_bytes_in_text,
    count_lines_in_text,
    count_words_in_text,
    count_characters_in_text,
)


class TestCountFunctions(unittest.TestCase):
    def test_count_bytes_in_text(self):
        text = "This is a test text."
        bytes_count = count_bytes_in_text(text)
        self.assertEqual(bytes_count, len(text.encode()))

    def test_count_lines_in_text(self):
        text = "Line 1\nLine 2\nLine 3"
        line_count = count_lines_in_text(text)
        self.assertEqual(line_count, 3)

    def test_count_words_in_text(self):
        text = "This is a test text."
        word_count = count_words_in_text(text)
        self.assertEqual(word_count, 5)

    def test_count_characters_in_text(self):
        text = "This is a test text."
        character_count = count_characters_in_text(text)
        self.assertEqual(character_count, len(text))


class TestCommandLineArguments(unittest.TestCase):
    def test_command_line_args(self):
        with patch("sys.argv", ["ccwc.py", "-c", "-l", "-w", "test.txt"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                from ccwc import main

                main()
                output = mock_stdout.getvalue()
                self.assertIn("Bytes count:", output)
                self.assertIn("Line count:", output)
                self.assertIn("Word count:", output)


if __name__ == "__main__":
    unittest.main()
