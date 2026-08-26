class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)
    
    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    
    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / \
            (other.real**2 + other.imaginary**2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / \
            (other.real**2 + other.imaginary**2)
        return ComplexNumber(real, imaginary)
    
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
