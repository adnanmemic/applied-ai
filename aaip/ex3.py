class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        return f"Greetings to {self.name}"
        
