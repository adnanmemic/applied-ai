from typing import Self


class Person:
    def __init__(self, name: str, age: int, address: str) -> None:
        """Initialize a person.

        Args:
            name: The name of the person.
            age: The age of the person.
            address: The address of the person.

        Raises:
            TypeError: If name is not a string, age is not an integer or address
                is not a string.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string!")

        if not isinstance(age, int):
            raise TypeError("age must be an integer!")

        if not isinstance(address, str):
            raise TypeError("address must be a string!")

        self.name = name
        self.age = age
        self.address = address

    def greet(self) -> str:
        """Greet the person by name.

        Returns:
            A greeting containing the person's name.
        """
        return f"Greetings to {self.name}"

    @classmethod
    def from_string(cls, person_string: str) -> Self:
        """Create a new object from a specified string.

        Args:
            person_string: A string containing the person's name, age and address.

        Returns:
            A new Person instance.

        Raises:
            TypeError: If person_string is not a string.
        """
        if not isinstance(person_string, str):
            raise TypeError("person_string must be a string")

        name, age, address = [x.strip() for x in person_string.split(",")]
        return cls(name, int(age), address)


class Student(Person):
    def __init__(self, name: str, age: int, address: str, university: str) -> None:
        """Initialize a person.

        Args:
            name: The name of the person.
            age: The age of the person.
            address: The address of the person.
            university: The university name of the person.

        Raises:
            TypeError: If name, address or university is not a string or age is
                not an integer.
        """
        super().__init__(name, age, address)
        if not isinstance(university, str):
            raise TypeError("university must be a string!")

        self.university = university

    def greet(self) -> str:
        """Greet the student by name.

        Returns:
            A greeting containing the student's name and university.
        """
        return f"Greetings to {self.name} and his university: {self.university}"
