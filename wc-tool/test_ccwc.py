import unittest
from unittest.mock import patch
from io import StringIO
from ccwc import (
    count_bytes_in_file,
    count_lines_in_file,
    count_words_in_file,
    count_characters_in_file,
)


class TestFileCountingFunctions(unittest.TestCase):
    def test_count_bytes_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_bytes_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"Bytes count: {342184}; File: test.txt")

    def test_count_lines_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_lines_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"Line count: {7143}; File: test.txt")

    def test_count_words_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_words_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"Word count: {58164}; File: test.txt")

    def test_count_characters_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_characters_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"Character count: {339286}; File: test.txt")

    def test_no_file_present(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_bytes_in_file("unknown.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"ccwc -c: unknown.txt: No such file or directory")


if __name__ == "__main__":
    unittest.main()
