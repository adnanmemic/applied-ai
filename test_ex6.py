import unittest
import os
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
        