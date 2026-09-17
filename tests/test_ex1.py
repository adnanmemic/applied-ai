import unittest
from unittest.mock import patch

from aaip import ex1


class TestHelloPython(unittest.TestCase):
    @patch("builtins.print")
    def test_hello_python_exercise(self, mock_print):
        ex1.hello_python_exercise(20, "John Doe")

        mock_print.assert_called_once_with(
            "This course has 20 and one of those is John Doe."
        )

    @patch("builtins.print")
    def test_hello_python_exercise_default(self, mock_print):
        ex1.hello_python_exercise(20)

        mock_print.assert_called_once_with(
            "This course has 20 and one of those is Adnan Memic."
        )

    def test_hello_python_exercise_wrong_num_students_type(self):
        with self.assertRaises(TypeError):
            ex1.hello_python_exercise("int", "John Doe")

    def test_hello_python_exercise_wrong_num_students_value(self):
        with self.assertRaises(ValueError):
            ex1.hello_python_exercise(-1, "John Doe")

    def test_hello_python_exercise_wrong_student_name_type(self):
        with self.assertRaises(TypeError):
            ex1.hello_python_exercise(20, 5)

    def test_hello_python_exercise_empty_student_name(self):
        values = ["", "   "]
        for value in values:
            with self.subTest(value=value), self.assertRaises(ValueError):
                ex1.hello_python_exercise(20, value)
