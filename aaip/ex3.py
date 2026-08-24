class Person:
    def __init__(self, name: str, age: int, address: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")

        if not isinstance(age, int):
            raise TypeError("Age must be an integer!")

        if not isinstance(address, str):
            raise TypeError("Address must be a string!")

        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        return f"Greetings to {self.name}"

    @classmethod
    def from_string(cls, person_string: str):
        if not isinstance(person_string, str):
            raise TypeError("Methodparameter must be a string")

        name, age, address = [x.strip() for x in person_string.split(",")]
        return cls(name, int(age), address)
        
class Student(Person):
    def __init__(self, name: str, age: int, address: str, university: str) -> None:
        super().__init__(name, age, address)
        if not isinstance(university, str):
            raise TypeError("University must be a string!")

        self.university = university

    def greet(self):
        return f"Greetings to {self.name} and his university: {self.university}"
