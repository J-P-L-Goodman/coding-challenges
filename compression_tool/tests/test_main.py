import unittest
from io import StringIO
from unittest.mock import patch


class TestCommandLineArguments(unittest.TestCase):
    def test_command_line_args(self):
        with patch("sys.argv", ["main.py", "gutenberg.txt"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                from main import main

                main()
                output = mock_stdout.getvalue()
                self.assertIn("333 occurances of X", output)
                self.assertIn("223000 occurances of t", output)


class TestHelperFunctions(unittest.TestCase):
    def test_number_of_occurances(self):
        from main import number_of_occurances

        text = "This is a test text."
        char_counts = number_of_occurances(text)
        self.assertEqual(char_counts.get("X"), None)
        self.assertEqual(char_counts.get("t"), 4)
        self.assertEqual(char_counts.get("i"), 2)
        self.assertEqual(char_counts.get("s"), 3)
        self.assertEqual(char_counts.get("."), 1)
