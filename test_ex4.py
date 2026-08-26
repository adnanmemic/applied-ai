import unittest
from aaip import ex4

class TestComplexNumber(unittest.TestCase):

    def setUp(self):
        self.a = ex4.ComplexNumber(4, 3)
        self.b = ex4.ComplexNumber(2, -1)
        self.c = ex4.ComplexNumber(0, 0)
        self.d = ex4.ComplexNumber(-3, -2)


    def test_addition(self):
        self.assertEqual(self.a + self.b, ex4.ComplexNumber(6, 2))
        self.assertEqual(self.a + self.c, ex4.ComplexNumber(4, 3))
        self.assertEqual(self.b + self.d, ex4.ComplexNumber(-1, -3))

    def test_subtraction(self):
        self.assertEqual(self.a - self.b, ex4.ComplexNumber(2, 4))
        self.assertEqual(self.a - self.c, ex4.ComplexNumber(4, 3))
        self.assertEqual(self.b - self.d, ex4.ComplexNumber(5, 1))

    def test_multiplication(self):
        self.assertEqual(self.a * self.b, ex4.ComplexNumber(11, 2))
        self.assertEqual(self.a * self.c, ex4.ComplexNumber(0, 0))
        self.assertEqual(self.b * self.d, ex4.ComplexNumber(-8, -1))

    def test_division(self):
        self.assertEqual(self.a / self.b, ex4.ComplexNumber(1, 2))
        self.assertEqual(self.b / self.d, ex4.ComplexNumber(-4/13, 7/13))
    
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.a / self.c