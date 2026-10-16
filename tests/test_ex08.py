import unittest

from applied_ai import ex08


class TestListAverage(unittest.TestCase):
    def test_average_positive_numbers(self):
        l1 = [5, 3, 9, 4, 20]  # integers
        l2 = [3.2, 9.4, 6.1, 50.6, 20.3]  # float
        self.assertAlmostEqual(ex08.list_average(l1), 8.2)  # type: ignore
        self.assertAlmostEqual(ex08.list_average(l2), 17.92)  # type: ignore

    def test_average_negative_numbers(self):
        l1 = [-5, -2, -6, -30, -25]
        l2 = [-20.1, -4.9, -15.3, -9.1, -6.5]
        self.assertAlmostEqual(ex08.list_average(l1), -13.6)  # type: ignore
        self.assertAlmostEqual(ex08.list_average(l2), -11.18)  # type: ignore

    def test_average_empty_list(self):
        l = []
        self.assertIsNone(ex08.list_average(l))

    def test_average_one_element_list(self):
        l1 = [5]
        l2 = [20.4]
        self.assertAlmostEqual(ex08.list_average(l1), 5.0)  # type: ignore
        self.assertAlmostEqual(ex08.list_average(l2), 20.4)  # type: ignore
