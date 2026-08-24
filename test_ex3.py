import unittest
from aaip import ex3

class TestPerson(unittest.TestCase):

    def test_greet_person(self):
        person = ex3.Person("John", 30, "Somestreet 50")
        self.assertEqual(person.greet(), "Greetings to John")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            ex3.Person(50, 26, "Anystreet 3")

    def test_invalid_age_type(self):
        with self.assertRaises(TypeError):
            ex3.Person("John", "26", "Anystreet 3")

    def test_invalid_address_type(self):
        with self.assertRaises(TypeError):
            ex3.Person("John", 26, 3)
    
    def test_greet_student(self):
        student = ex3.Student("John", 30, "Somestreet 50", "Uni")
        self.assertEqual(student.greet(), "Greetings to John and his university: Uni")

    def test_invalid_university_type(self):
        with self.assertRaises(TypeError):
            ex3.Student("John", 26, "Anystreet 3", 5)
    
    def test_from_string_attribute_values(self):
        person = ex3.Person.from_string("John, 26, Somestreet 50")
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 26)
        self.assertEqual(person.address, "Somestreet 50")
    
    def test_from_string_returns_person(self):
        person = ex3.Person.from_string("John, 26, Somestreet 50")
        self.assertIsInstance(person, ex3.Person)
    
    def test_from_string_invalid_type(self):
        with self.assertRaises(TypeError):
            ex3.Person.from_string(5)

