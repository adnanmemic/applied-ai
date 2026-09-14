import os
import unittest
from tempfile import TemporaryDirectory

from aaip import ex7


class FileManagerTestCases(unittest.TestCase):
    def setUp(self):
        with TemporaryDirectory(delete=False) as tmpdir:
            self.root_path = tmpdir

        # create directories
        dir_paths = {
            # directory to copy file into
            "copy_dir1": "copy-dir/copy1",
            "copy_dir2": "copy-dir/copy2",
            "copy_dir3": "copy-dir/copy3",
            # directory to move file into
            "move_dir": "move-dir",
        }

        # join 
        self.full_dir_paths = {
            key: os.path.join(self.root_path, path) for key, path in dir_paths.items()
        }

        # creates all needed directories
        for joined_dir_path in self.full_dir_paths.values():
            os.makedirs(joined_dir_path, exist_ok=True)

        # paths of the created directories
        self.copy_dir_paths = [
            self.full_dir_paths["copy_dir1"],
            self.full_dir_paths["copy_dir2"],
            self.full_dir_paths["copy_dir3"],
        ]
        self.move_dir_path = self.full_dir_paths["move_dir"]

        # create test file
        self.test_file_name = "test_file.txt"
        self.test_file_path = os.path.join(self.root_path, self.test_file_name)
        with open(self.test_file_path, "w"):
            pass

    def tearDown(self):
        for dirpath, _, filenames in os.walk(self.root_path, topdown=False):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                os.remove(full_file_path)
            os.rmdir(dirpath)

    def test_copy_file(self):
        ex7.copy_file(self.test_file_path, self.copy_dir_paths)

        for path in self.copy_dir_paths:
            # paths of the copied files
            copied_file_path = os.path.join(path, self.test_file_name)

            with self.subTest(copied_file_path=copied_file_path):
                self.assertTrue(os.path.isfile(copied_file_path))
