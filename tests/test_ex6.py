import os
import unittest
from tempfile import NamedTemporaryFile
from unittest.mock import patch

from aaip import ex6


class TestCommandLineTool(unittest.TestCase):
    def setUp(self):
        # delete = false doesn't delete the file when being closed
        with NamedTemporaryFile(mode="w", encoding="utf-8", delete=False) as file:
            self.file_path = file.name
            file.write("This is a sentence\nand a test\n")

    def tearDown(self):
        os.remove(self.file_path)

    def test_count_words(self):
        word_count = ex6.count_words(self.file_path)
        self.assertEqual(word_count, 7)

    def test_count_lines(self):
        line_count = ex6.count_lines(self.file_path)
        self.assertEqual(line_count, 2)

    def test_search_word(self):
        line_list = ex6.search_word(self.file_path, "sentence")
        self.assertEqual(line_list, ["This is a sentence"])

    def test_search_word_with_empty_word(self):
        with self.assertRaises(ValueError):
            ex6.search_word(self.file_path, "")
        with self.assertRaises(ValueError):
            ex6.search_word(self.file_path, "   ")

    @patch("builtins.print")
    @patch("sys.argv", new_callable=list)
    def test_main_count_words(self, mock_argv, mock_print):
        mock_argv.extend(["aaip/ex6.py", self.file_path, "count_words"])
        ex6.main()
        mock_print.assert_called_once_with("Words: ", 7)

    @patch("builtins.print")
    @patch("sys.argv", new_callable=list)
    def test_main_count_lines(self, mock_argv, mock_print):
        mock_argv.extend(["aaip/ex6.py", self.file_path, "count_lines"])
        ex6.main()
        mock_print.assert_called_once_with("Lines: ", 2)

    @patch("builtins.print")
    @patch("sys.argv", new_callable=list)
    def test_main_search_word(self, mock_argv, mock_print):
        mock_argv.extend(["aaip/ex6.py", self.file_path, "search_word", "sentence"])
        ex6.main()
        mock_print.assert_called_once_with("This is a sentence")

    @patch("sys.argv", new_callable=list)
    def test_main_missing_second_argument(self, mock_argv):
        mock_argv.extend(["aaip/ex6.py", self.file_path])
        with self.assertRaises(SystemExit) as context:
            ex6.main()

        self.assertEqual(context.exception.code, 2)

    @patch("sys.argv", new_callable=list)
    def test_main_missing_third_argument(self, mock_argv):
        mock_argv.extend(["aaip/ex6.py", self.file_path, "search_word"])
        with self.assertRaises(SystemExit) as context:
            ex6.main()

        self.assertEqual(context.exception.code, 2)

    @patch("sys.argv", new_callable=list)
    def test_main_wrong_action(self, mock_argv):
        mock_argv.extend(["aaip/ex6.py", self.file_path, "count_anything"])
        with self.assertRaises(SystemExit) as context:
            ex6.main()

        self.assertEqual(context.exception.code, 2)

    @patch("sys.argv", new_callable=list)
    def test_main_file_not_found(self, mock_argv):
        non_existing_file = "hello"
        mock_argv.extend(["aaip/ex6.py", non_existing_file, "count_words"])
        with self.assertRaises(SystemExit) as context:
            ex6.main()

        self.assertEqual(context.exception.code, 1)

    @patch("sys.argv", new_callable=list)
    def test_main_word_is_empty_or_whitespace(self, mock_argv):
        mock_argv.extend(["aaip/ex6.py", self.file_path, "search_word", " "])
        with self.assertRaises(SystemExit) as context:
            ex6.main()

        self.assertEqual(context.exception.code, 2)
