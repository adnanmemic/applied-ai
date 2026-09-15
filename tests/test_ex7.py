import os
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

from aaip import ex7


class FileManagerTestCases(unittest.TestCase):
    def setUp(self):
        with TemporaryDirectory(delete=False) as tmpdir:
            self.root_path = tmpdir

        # create directories
        copy_dir_paths = [
            "copy-dir/copy1",
            "copy-dir/copy2",
            "copy-dir/copy3",
        ]
        # directory to move file into
        self.full_move_dir_path = os.path.join(self.root_path, "move-dir")

        self.full_copy_dir_paths = [
            os.path.join(self.root_path, copy_dir_path)
            for copy_dir_path in copy_dir_paths
        ]

        # creates all needed directories
        for full_copy_dir_path in self.full_copy_dir_paths:
            os.makedirs(full_copy_dir_path, exist_ok=True)
        os.makedirs(self.full_move_dir_path, exist_ok=True)

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
        ex7.copy_file(self.test_file_path, self.full_copy_dir_paths)

        for full_copy_dir_path in self.full_copy_dir_paths:
            # paths of the copied files
            copied_file_path = os.path.join(full_copy_dir_path, self.test_file_name)

            with self.subTest(copied_file_path=copied_file_path):
                self.assertTrue(os.path.isfile(copied_file_path))

    def test_copy_file_empty_src_path(self):
        with self.assertRaises(ValueError):
            ex7.copy_file("", self.full_copy_dir_paths)

    def test_copy_file_empty_destination_path(self):
        with self.assertRaises(ValueError):
            ex7.copy_file(self.test_file_path, [""])

    def test_move_file(self):
        ex7.move_file(self.test_file_path, self.full_move_dir_path)

        moved_file_path = os.path.join(self.full_move_dir_path, self.test_file_name)
        self.assertTrue(os.path.isfile(moved_file_path))

    def test_move_file_empty_src_path(self):
        with self.assertRaises(ValueError):
            ex7.move_file("", self.full_move_dir_path)

    def test_move_file_empty_destination_path(self):
        with self.assertRaises(ValueError):
            ex7.move_file(self.test_file_path, "")

    def test_rename_file(self):
        new_file_name = "another_name.txt"
        new_file_path = os.path.join(self.root_path, new_file_name)

        ex7.rename_file(self.test_file_path, new_file_path)
        self.assertTrue(os.path.isfile(new_file_path))

    def test_rename_file_empty_src_path(self):
        new_file_name = "another_name.txt"
        new_file_path = os.path.join(self.root_path, new_file_name)

        with self.assertRaises(ValueError):
            ex7.rename_file("", new_file_path)

    def test_rename_file_empty_destination_path(self):
        with self.assertRaises(ValueError):
            ex7.rename_file(self.test_file_path, "")

    def test_check_dst_len_not_one_destination(self):
        values = [[], ["dir1", "dir2"]]
        for value in values:
            with self.subTest(value=value):
                self.assertTrue(ex7.check_dst_len(value))

    def test_check_dst_len_one_destination(self):
        self.assertFalse(ex7.check_dst_len(["dir"]))

    @patch("sys.argv", new_callable=list)
    def test_main_copy(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "copy",
                "--src",
                self.test_file_path,
                "--dst",
                self.full_copy_dir_paths[0],
                self.full_copy_dir_paths[1],
                self.full_copy_dir_paths[2],
            ]
        )
        ex7.main()

        for full_copy_dir_path in self.full_copy_dir_paths:
            # paths of the copied files
            copied_file_path = os.path.join(full_copy_dir_path, self.test_file_name)

            with self.subTest(copied_file_path=copied_file_path):
                self.assertTrue(os.path.isfile(copied_file_path))

    @patch("sys.argv", new_callable=list)
    def test_main_move(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "move",
                "--src",
                self.test_file_path,
                "--dst",
                self.full_move_dir_path,
            ]
        )
        ex7.main()

        moved_file_path = os.path.join(self.full_move_dir_path, self.test_file_name)
        self.assertTrue(os.path.isfile(moved_file_path))

    @patch("sys.argv", new_callable=list)
    def test_main_rename(self, mock_argv):
        new_file_name = "another_name.txt"
        new_file_path = os.path.join(self.root_path, new_file_name)

        mock_argv.extend(
            [
                "aaip/ex7.py",
                "rename",
                "--src",
                self.test_file_path,
                "--dst",
                new_file_path,
            ]
        )

        ex7.main()

        renamed_file_path = os.path.join(self.root_path, new_file_path)
        self.assertTrue(os.path.isfile(renamed_file_path))

    @patch("sys.argv", new_callable=list)
    def test_main_move_to_more_than_one_dst(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "move",
                "--src",
                self.test_file_path,
                "--dst",
                "dir1",
                "dir2",
            ]
        )

        with self.assertRaises(SystemExit) as e:
            ex7.main()

        self.assertEqual(e.exception.code, 2)

    @patch("sys.argv", new_callable=list)
    def test_main_rename_to_more_than_one_dst(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "rename",
                "--src",
                self.test_file_path,
                "--dst",
                "file1",
                "file2",
            ]
        )

        with self.assertRaises(SystemExit) as e:
            ex7.main()

        self.assertEqual(e.exception.code, 2)

    @patch("sys.argv", new_callable=list)
    def test_main_wrong_positional_arg(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "chmod",
                "--src",
                self.test_file_path,
                "--dst",
                "file1",
                "file2",
            ]
        )

        with self.assertRaises(SystemExit) as e:
            ex7.main()

        self.assertEqual(e.exception.code, 1)

    @patch("sys.argv", new_callable=list)
    def test_main_empty_source(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "copy",
                "--src",
                "",
                "--dst",
                "file1",
                "file2",
            ]
        )

        with self.assertRaises(SystemExit) as e:
            ex7.main()

        self.assertEqual(e.exception.code, 1)

    @patch("sys.argv", new_callable=list)
    def test_main_empty_destination(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "copy",
                "--src",
                self.test_file_path,
                "--dst",
                "",
            ]
        )

        with self.assertRaises(SystemExit) as e:
            ex7.main()

        self.assertEqual(e.exception.code, 1)

    @patch("sys.argv", new_callable=list)
    def test_main_file_not_found_error(self, mock_argv):
        mock_argv.extend(
            [
                "aaip/ex7.py",
                "copy",
                "--src",
                "file_does_not_exist",
                "--dst",
                "file1",
                "file2",
            ]
        )

        with self.assertRaises(SystemExit) as e:
            ex7.main()

        self.assertEqual(e.exception.code, 1)
