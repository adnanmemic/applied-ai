import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from aaip import ex2


class TestStudentDatabase(unittest.TestCase):
    def setUp(self):
        self.database = [
            {"id": "1", "name": "John", "grade": "5"},
            {"id": "2", "name": "Trevor", "grade": "4"},
            {"id": "3", "name": "Sergei", "grade": "2"},
            {"id": "4", "name": "Ivan", "grade": "1"},
        ]

        self.empty_database = []

    def test_get_students_from_csv(self):
        content = self.database

        with TemporaryDirectory() as tmpdir:
            path_name = str(Path(tmpdir) / "data.csv")

            with open(path_name, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "name", "grade"]
                csv_writer = csv.DictWriter(file, fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(content)

            database = ex2.get_students_from_csv(path_name)

            self.assertEqual(database, content)

    def test_add_student(self):
        with patch("builtins.input", side_effect=["Bob", "3", ""]):
            ex2.add_student(self.database)

        self.assertEqual(self.database[-1], {"id": "5", "name": "Bob", "grade": "3"})

    def test_add_student_wrong_grade_type(self):
        with patch("builtins.input", side_effect=["Bob", "not_a_number", ""]):
            ex2.add_student(self.empty_database)

        self.assertEqual(self.empty_database, [])

    def test_add_student_grade_out_of_range(self):
        with patch("builtins.input", side_effect=["Bob", "0", ""]):
            ex2.add_student(self.empty_database)

        with patch("builtins.input", side_effect=["Bob", "6", ""]):
            ex2.add_student(self.empty_database)

        self.assertEqual(self.empty_database, [])

    def test_add_student_to_empty_database(self):
        with patch("builtins.input", side_effect=["Bob", "3", ""]):
            ex2.add_student(self.empty_database)

        self.assertEqual(self.empty_database[0]["id"], "1")

    def test_search_student(self):
        self.assertEqual(
            ex2.search_student(self.database, student_id=3),
            {"id": "3", "name": "Sergei", "grade": "2"},
        )

        self.assertEqual(
            ex2.search_student(self.database, name="Trevor"),
            {"id": "2", "name": "Trevor", "grade": "4"},
        )

    def test_search_student_empty_database(self):
        self.assertIsNone(ex2.search_student(self.empty_database, student_id=5))
        self.assertIsNone(ex2.search_student(self.empty_database, name="Josh"))

    def test_search_student_wrong_student_id_type(self):
        with self.assertRaises(TypeError):
            ex2.search_student(self.database, student_id="two")

    def test_search_student_wrong_student_id_number(self):
        with self.assertRaises(ValueError):
            ex2.search_student(self.database, student_id=0)

    def test_search_student_wrong_name_type(self):
        with self.assertRaises(TypeError):
            ex2.search_student(self.database, name=5)

    def test_search_student_empty_name(self):
        with self.assertRaises(ValueError):
            ex2.search_student(self.database, name="")

        with self.assertRaises(ValueError):
            ex2.search_student(self.database, name="   ")

    def test_search_student_with_no_name_no_id(self):
        with self.assertRaises(ValueError):
            ex2.search_student(self.database)

    def test_no_student_was_found(self):
        self.assertIsNone(ex2.search_student(self.database, student_id=5))
        self.assertIsNone(ex2.search_student(self.database, name="Josh"))

    def test_change_grade(self):
        ex2.change_grade(self.database, 1, 2)

        self.assertEqual(self.database[0], {"id": "1", "name": "John", "grade": "2"})

    def test_change_grade_with_empty_database(self):
        with self.assertRaises(ValueError):
            ex2.change_grade(self.empty_database, 2, 3)

    def test_change_grade_wrong_student_id_type(self):
        with self.assertRaises(TypeError):
            ex2.change_grade(self.database, "two", 3)

    def test_change_grade_wrong_grade_type(self):
        with self.assertRaises(TypeError):
            ex2.change_grade(self.database, 2, "three")

    def test_change_grade_wrong_student_id_range(self):
        with self.assertRaises(ValueError):
            ex2.change_grade(self.database, 0, 3)

    def test_change_grade_wrong_grade_range(self):
        with self.assertRaises(ValueError):
            ex2.change_grade(self.database, 2, 0)

        with self.assertRaises(ValueError):
            ex2.change_grade(self.database, 2, 6)

    def test_store_students_into_csv(self):
        file_content = []

        with TemporaryDirectory() as tmpdir:
            path_name = str(Path(tmpdir) / "data.csv")
            ex2.store_students_into_csv(self.database, path_name)

            with open(path_name, "r", encoding="utf-8", newline="") as file:
                file_content = list(csv.DictReader(file))

        self.assertEqual(file_content, self.database)
