import os
import unittest
from tempfile import NamedTemporaryFile
from unittest.mock import patch

from applied_ai import ex6


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
        values = ["", "   "]

        for value in values:
            with self.subTest(value=value), self.assertRaises(ValueError):
                ex6.search_word(self.file_path, value)

    @patch("applied_ai.ex6.count_words")
    @patch("builtins.print")
    @patch("sys.argv", new_callable=list)
    def test_main_count_words(self, mock_argv, mock_print, mock_count_words):
        mock_count_words.return_value = 7 
        mock_argv.extend(["aaip/ex6.py", self.file_path, "count_words"])

        ex6.main()

        mock_count_words.assert_called_once_with(self.file_path)
        mock_print.assert_called_once_with("Words: ", 7)

    @patch("applied_ai.ex6.count_lines")
    @patch("builtins.print")
    @patch("sys.argv", new_callable=list)
    def test_main_count_lines(self, mock_argv, mock_print, mock_count_lines):
        mock_count_lines.return_value = 2 
        mock_argv.extend(["aaip/ex6.py", self.file_path, "count_lines"])

        ex6.main()

        mock_count_lines.assert_called_once_with(self.file_path)
        mock_print.assert_called_once_with("Lines: ", 2)

    @patch("applied_ai.ex6.search_word")
    @patch("builtins.print")
    @patch("sys.argv", new_callable=list)
    def test_main_search_word(self, mock_argv, mock_print, mock_search_word):
        word = "sentence"
        mock_search_word.return_value = ["This is a sentence"]
        mock_argv.extend(["aaip/ex6.py", self.file_path, "search_word", word])

        ex6.main()

        mock_search_word.assert_called_once_with(self.file_path, word)
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

    @patch("applied_ai.ex6.count_words")
    @patch("sys.argv", new_callable=list)
    def test_main_file_not_found(self, mock_argv, mock_count_words):
        non_existing_file = "hello"
        mock_count_words.side_effect = FileNotFoundError
        mock_argv.extend(["aaip/ex6.py", non_existing_file, "count_words"])

        with self.assertRaises(SystemExit) as context:
            ex6.main()

        mock_count_words.assert_called_once_with(non_existing_file)
        self.assertEqual(context.exception.code, 1)

    @patch("applied_ai.ex6.search_word")
    @patch("sys.argv", new_callable=list)
    def test_main_word_is_empty_or_whitespace(self, mock_argv, mock_search_word):
        values = ["", "  "]
        mock_search_word.side_effect = ValueError

        for value in values: 
            mock_argv[:] = ["aaip/ex6.py", self.file_path, "search_word", value]
            with self.subTest(value=value):
                with self.assertRaises(SystemExit) as context:
                    ex6.main()

                self.assertEqual(context.exception.code, 2)

