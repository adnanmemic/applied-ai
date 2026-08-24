import unittest
from aaip import ex3

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person1 = ex3.Person("John", 30, "Somestreet 50")

    def test_greet_person(self):
        self.assertEqual(self.person1.greet(), "Greetings to John")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            ex3.Person(50, 26, "Anystreet 3")

    def test_invalid_age_type(self):
        with self.assertRaises(TypeError):
            ex3.Person("John", "26", "Anystreet 3")

    def test_invalid_address_type(self):
        with self.assertRaises(TypeError):
            ex3.Person("John", 26, 3)
