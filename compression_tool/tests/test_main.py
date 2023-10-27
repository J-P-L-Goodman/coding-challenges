import unittest
from io import StringIO
from unittest.mock import patch


class TestCommandLineArguments(unittest.TestCase):
    def test_command_line_args(self):
        with patch("sys.argv", ["main.py", "test.txt"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                from main import main

                main()
                output = mock_stdout.getvalue()
                self.assertIn("Bytes count:", output)
