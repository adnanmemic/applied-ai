import unittest

from applied_ai import ex04


class TestComplexNumber(unittest.TestCase):
    def setUp(self):
        self.a = ex04.ComplexNumber(4, 3)
        self.b = ex04.ComplexNumber(2, -1)
        self.c = ex04.ComplexNumber(0, 0)
        self.d = ex04.ComplexNumber(-3, -2)

    def test_addition(self):
        self.assertEqual(self.a + self.b, ex04.ComplexNumber(6, 2))
        self.assertEqual(self.a + self.c, ex04.ComplexNumber(4, 3))
        self.assertEqual(self.b + self.d, ex04.ComplexNumber(-1, -3))

    def test_subtraction(self):
        self.assertEqual(self.a - self.b, ex04.ComplexNumber(2, 4))
        self.assertEqual(self.a - self.c, ex04.ComplexNumber(4, 3))
        self.assertEqual(self.b - self.d, ex04.ComplexNumber(5, 1))

    def test_multiplication(self):
        self.assertEqual(self.a * self.b, ex04.ComplexNumber(11, 2))
        self.assertEqual(self.a * self.c, ex04.ComplexNumber(0, 0))
        self.assertEqual(self.b * self.d, ex04.ComplexNumber(-8, -1))

    def test_division(self):
        self.assertEqual(self.a / self.b, ex04.ComplexNumber(1, 2))
        self.assertEqual(self.b / self.d, ex04.ComplexNumber(-4 / 13, 7 / 13))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.a / self.c

    def test_wrong_input_constructor(self):
        with self.assertRaises(TypeError):
            ex04.ComplexNumber("foo", 5)

        with self.assertRaises(TypeError):
            ex04.ComplexNumber(5, "foo")

        with self.assertRaises(TypeError):
            ex04.ComplexNumber("foo", "bar")

    def test_wrong_input_addition(self):
        with self.assertRaises(TypeError):
            self.a + "foo"

    def test_wrong_input_subtraction(self):
        with self.assertRaises(TypeError):
            self.a - "foo"

    def test_wrong_input_multiplication(self):
        with self.assertRaises(TypeError):
            self.a * "foo"

    def test_wrong_input_division(self):
        with self.assertRaises(TypeError):
            self.a / "foo"

    def test_wrong_input_equal(self):
        self.assertFalse(self.a == "foo")

    def test_print_complex_number(self):
        self.e = ex04.ComplexNumber(0, -2)
        self.f = ex04.ComplexNumber(4, 0)

        self.assertEqual(str(self.a), "4 + 3i")
        self.assertEqual(str(self.b), "2 - 1i")
        self.assertEqual(str(self.c), "0")
        self.assertEqual(str(self.d), "-3 - 2i")
        self.assertEqual(str(self.e), "-2i")
        self.assertEqual(str(self.f), "4")

    def test_sum_of_complex_numbers(self):
        complex_number = [self.a, self.b, self.c, self.d]

        empty_list = []

        self.assertEqual(
            ex04.complex_number_sum(complex_number), ex04.ComplexNumber(3, 0)
        )
        self.assertEqual(ex04.complex_number_sum(empty_list), ex04.ComplexNumber(0, 0))
