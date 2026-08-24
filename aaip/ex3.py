class Person:
    def __init__(self, name: str, age: int, address: str):
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
        
