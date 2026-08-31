import os
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

from aaip import ex5


class TestDirectoryManagement(unittest.TestCase):
    def test_create_project_wrong_base_path_type(self):
        with self.assertRaises(TypeError):
            ex5.create_project_structure(5, "new_project")

    def test_create_project_wrong_project_name_type(self):
        with self.assertRaises(TypeError):
            ex5.create_project_structure("project_path", 5)

    def test_create_project_empty_base_path(self):
        with self.assertRaises(ValueError):
            ex5.create_project_structure("", "new_project")
        with self.assertRaises(ValueError):
            ex5.create_project_structure("  ", "new_project")

    def test_create_project_empty_project_name(self):
        with self.assertRaises(ValueError):
            ex5.create_project_structure("project_path", "")
        with self.assertRaises(ValueError):
            ex5.create_project_structure("project_path", "  ")

    @patch("builtins.print")
    def test_project_path_already_exists(self, mock_print):
        with TemporaryDirectory() as tmpdir:
            project_name = "new_project"

            ex5.create_project_structure(tmpdir, project_name)
            ex5.create_project_structure(tmpdir, project_name)

            mock_print.assert_called_once_with("Project already exists!")

    def test_create_project_structure(self):
        with TemporaryDirectory() as tmpdir:
            project_name = "new_project"
            ex5.create_project_structure(tmpdir, project_name)

            # Test existence of src directory
            self.assertTrue(os.path.isdir(os.path.join(tmpdir, project_name, "src")))

            # Test existence of docs directory
            self.assertTrue(os.path.isdir(os.path.join(tmpdir, project_name, "docs")))

            # Test existence of README.md
            self.assertTrue(
                os.path.isfile(os.path.join(tmpdir, project_name, "README.md"))
            )

            # Test existence of main.py
            self.assertTrue(
                os.path.isfile(os.path.join(tmpdir, project_name, "src", "main.py"))
            )

    def test_readme_content(self):
        with TemporaryDirectory() as tmpdir:
            project_name = "new_project"
            ex5.create_project_structure(tmpdir, project_name)
            readme_path = os.path.join(tmpdir, project_name, "README.md")

            with open(readme_path, "r", encoding="utf-8") as file:
                self.assertEqual(
                    file.read(), f"# {project_name}\n\nDescription of your project"
                )

    def test_main_content(self):
        with TemporaryDirectory() as tmpdir:
            project_name = "new_project"
            ex5.create_project_structure(tmpdir, project_name)
            main_path = os.path.join(tmpdir, project_name, "src", "main.py")

            with open(main_path, "r", encoding="utf-8") as file:
                self.assertEqual(file.read(), 'print("Hello, World!")')

    @patch("builtins.print")
    def test_traverse_directory(self, mock_print):
        with TemporaryDirectory() as tmpdir:
            path1 = os.path.join(tmpdir, "src")
            os.makedirs(path1)

            file1 = os.path.join(path1, "main.py")

            with open(file1, "w"):
                pass

            ex5.traverse_directory(tmpdir)

            mock_print.assert_any_call(f"Current directory: {tmpdir}")
            mock_print.assert_any_call("Directories: src")
            mock_print.assert_any_call("Files: -")

            mock_print.assert_any_call(f"Current directory: {path1}")
            mock_print.assert_any_call("Directories: -")
            mock_print.assert_any_call("Files: main.py")

    def test_traverse_directory_wrong_input_type(self):
        with self.assertRaises(TypeError):
            ex5.traverse_directory(5)

    def test_traverse_directory_empty_input_string(self):
        with self.assertRaises(ValueError):
            ex5.traverse_directory("")
        with self.assertRaises(ValueError):
            ex5.traverse_directory("  ")
