import unittest
from aaip import ex8

class TestListAverage(unittest.TestCase):

    def test_average_positive_numbers(self):
        l1 = [5, 3, 9, 4, 20] # integers
        l2 = [3.2, 9.4, 6.1, 50.6, 20.3] # float
        self.assertAlmostEqual(ex8.list_average(l1), 8.2)
        self.assertAlmostEqual(ex8.list_average(l2), 17.92)

    def test_average_negative_numbers(self):
        l1 = [-5, -2, -6, -30, -25]
        l2 = [-20.1, -4.9, -15.3, -9.1, -6.5]
        self.assertAlmostEqual(ex8.list_average(l1), -13.6)
        self.assertAlmostEqual(ex8.list_average(l2), -11.18)

    def test_average_empty_list(self):
        l = []
        self.assertIsNone(ex8.list_average(l))

    def test_average_one_element_list(self):
        l1 = [5]
        l2 = [20.4]
        self.assertAlmostEqual(ex8.list_average(l1), 5.0)
        self.assertAlmostEqual(ex8.list_average(l2), 20.4)