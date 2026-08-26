class ComplexNumber:
    def __init__(self, real, imaginary):
        if not isinstance(real, (int, float)):
            raise TypeError("Real must be a number!")

        if not isinstance(imaginary, (int, float)):
            raise TypeError("Imaginary must be a number!")

        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented

        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)
    
    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented

        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
            
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    
    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented

        if other.real == 0 and other.imaginary == 0:
            raise ZeroDivisionError("Can not divide by zero!")

        real = (self.real * other.real + self.imaginary * other.imaginary) / \
            (other.real**2 + other.imaginary**2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / \
            (other.real**2 + other.imaginary**2)
        return ComplexNumber(real, imaginary)
    
    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented

        return self.real == other.real and self.imaginary == other.imaginary
