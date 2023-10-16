import unittest
from unittest.mock import patch
from io import StringIO
from ccwc import count_bytes_in_file, count_lines_in_file, count_words_in_file


class TestFileCountingFunctions(unittest.TestCase):
    def test_count_bytes_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_bytes_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"Bytes count: {342190}; File: test.txt")

    def test_count_lines_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_lines_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"Line count: {7145}; File: test.txt")

    def test_count_words_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_words_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"Word count: {58164}; File: test.txt")

    def test_no_file_present(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_bytes_in_file("unknown.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, f"ccwc -c: unknown.txt: No such file or directory")


if __name__ == "__main__":
    unittest.main()
