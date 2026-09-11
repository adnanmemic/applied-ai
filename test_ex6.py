import os
import unittest
from tempfile import NamedTemporaryFile

from aaip import ex6


class TestCommanLineTool(unittest.TestCase):
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
