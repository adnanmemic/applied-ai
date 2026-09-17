import csv
import os
import unittest
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
        file_content = self.database

        with TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "data.csv")

            with open(file_path, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "name", "grade"]
                csv_writer = csv.DictWriter(file, fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(file_content)

            database = ex2.get_students_from_csv(file_path)

            self.assertEqual(database, file_content)

    @patch("builtins.input")
    def test_add_student(self, mock_input):
        mock_input.side_effect = ["Bob", "3", ""]
        ex2.add_student(self.database)

        self.assertEqual(self.database[-1], {"id": "5", "name": "Bob", "grade": "3"})

    @patch("builtins.input")
    def test_add_student_wrong_grade_type(self, mock_input):
        mock_input.side_effect = ["Bob", "not_a_number", ""]
        ex2.add_student(self.empty_database)

        self.assertEqual(self.empty_database, [])

    @patch("builtins.input")
    def test_add_student_grade_out_of_range(self, mock_input):
        values = [("Bob", "0", ""), ("Bob", "6", "")]

        for value in values:
            with self.subTest(value=value):
                mock_input.side_effect = value
                ex2.add_student(self.empty_database)

                self.assertEqual(self.empty_database, [])

    @patch("builtins.input")
    def test_add_student_to_empty_database(self, mock_input):
        mock_input.side_effect = ["Bob", "3", ""]
        ex2.add_student(self.empty_database)

        # The id of the first student must be 1
        self.assertEqual(self.empty_database[0]["id"], "1")

    def test_search_student_for_id(self):
        self.assertEqual(
            ex2.search_student(self.database, student_id=3),
            {"id": "3", "name": "Sergei", "grade": "2"},
        )

    def test_search_student_for_name(self):
        self.assertEqual(
            ex2.search_student(self.database, name="Trevor"),
            {"id": "2", "name": "Trevor", "grade": "4"},
        )

    def test_search_student_for_name_in_empty_database(self):
        self.assertIsNone(ex2.search_student(self.empty_database, student_id=5))

    def test_search_student_for_id_in_empty_database(self):
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
        values = ["", "   "]
        for value in values:
            with self.subTest(value=value), self.assertRaises(ValueError):
                ex2.search_student(self.database, name=value)

    def test_search_student_with_no_name_no_id(self):
        with self.assertRaises(ValueError):
            ex2.search_student(self.database)

    def test_no_student_was_found_id(self):
        self.assertIsNone(ex2.search_student(self.database, student_id=5))

    def test_no_student_was_found_name(self):
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
        values = [0, 6]
        for value in values:
            with self.subTest(value=value), self.assertRaises(ValueError):
                ex2.change_grade(self.database, 2, value)

    def test_store_students_into_csv(self):
        file_content = []

        with TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "data.csv")

            ex2.store_students_into_csv(self.database, file_path)
            with open(file_path, "r", encoding="utf-8", newline="") as file:
                file_content = list(csv.DictReader(file))

        self.assertEqual(file_content, self.database)
