import os
import unittest
from tempfile import TemporaryDirectory


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

        self.joined_dir_paths = {
            key: os.path.join(self.root_path, path) for key, path in dir_paths.items()
        }

        for joined_dir_path in self.joined_dir_paths.values():
            os.makedirs(joined_dir_path, exist_ok=True)

        # create test file
        test_file_name = "test_file.txt"
        test_file_path = os.path.join(self.root_path, test_file_name)
        with open(test_file_path, "w"):
            pass

    def tearDown(self):
        for dirpath, _, filenames in os.walk(self.root_path, topdown=False):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                os.remove(full_file_path)
            os.rmdir(dirpath)
