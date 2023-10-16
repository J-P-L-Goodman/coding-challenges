import unittest
from unittest.mock import patch
from io import StringIO
from ccwc import count_bytes_in_file, count_lines_in_file


class TestFileCountingFunctions(unittest.TestCase):
    def test_count_bytes_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_bytes_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            print(output)
            self.assertEqual(output, f"Bytes count: {342190}; File: test.txt")

    def test_count_lines_in_file(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            count_lines_in_file("test.txt")
            output = mock_stdout.getvalue().strip()
            print(output)
            self.assertEqual(output, f"Line count: {7145}; File: test.txt")


if __name__ == "__main__":
    unittest.main()
