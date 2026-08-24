import unittest
from aaip import ex3

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person1 = ex3.Person("John", 30, "Somestreet 50")

    def test_greet_person(self):
        self.assertEqual(self.person1.greet(), "Greetings to John")
