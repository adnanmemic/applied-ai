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

    def test_search_student(self):
        self.assertEqual(
            ex2.search_student(self.database, student_id=3),
            {"id": "3", "name": "Sergei", "grade": "2"},
        )

        self.assertEqual(
            ex2.search_student(self.database, name="Trevor"),
            {"id": "2", "name": "Trevor", "grade": "4"},
        )

    def test_change_grade(self):
        ex2.change_grade(self.database, 1, 2)

        self.assertEqual(self.database[0], {"id": "1", "name": "John", "grade": "2"})

    def test_store_students_into_csv(self):
        file_content = []

        with TemporaryDirectory() as tmpdir:
            path_name = str(Path(tmpdir) / "data.csv")
            ex2.store_students_into_csv(self.database, path_name)

            with open(path_name, "r", encoding="utf-8", newline="") as file:
                file_content = list(csv.DictReader(file))

        self.assertEqual(file_content, self.database)
