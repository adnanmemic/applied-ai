from __future__ import annotations  # postpones evaluation of type hints

from types import NotImplementedType


class ComplexNumber:
    def __init__(self, real: float, imaginary: float) -> None:
        """Initialize a complex number.

        Args:
            real: The real part of the complex number.
            imaginary: The imaginary part of the complex number.

        Raises:
            TypeError: If real or imaginary is not an integer or float.
        """
        if not isinstance(real, (int, float)):
            raise TypeError("Real must be a number!")

        if not isinstance(imaginary, (int, float)):
            raise TypeError("Imaginary must be a number!")

        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: ComplexNumber) -> ComplexNumber | NotImplementedType:
        """Add another complex number.

        Args:
            other: The complex number to add.

        Returns:
            A new ComplexNumber containing the sum, or NotImplemented if other
            is not a ComplexNumber.
        """
        if not isinstance(other, ComplexNumber):
            return NotImplemented  # eventually TypeError

        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __sub__(self, other: ComplexNumber) -> ComplexNumber | NotImplementedType:
        """Subtract another complex number.

        Args:
            other: The complex number to subtract.

        Returns:
            A new ComplexNumber containing the difference, or NotImplemented if
            other is not a ComplexNumber.
        """
        if not isinstance(other, ComplexNumber):
            return NotImplemented  # eventually TypeError

        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other: ComplexNumber) -> ComplexNumber | NotImplementedType:
        """Multiply by another complex number.

        Args:
            other: The complex number to multiply by.

        Returns:
            A new ComplexNumber containing the product, or NotImplemented if
            other is not a ComplexNumber.
        """
        if not isinstance(other, ComplexNumber):
            return NotImplemented  # eventually TypeError

        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other: ComplexNumber) -> ComplexNumber | NotImplementedType:
        """Divide by another complex number.

        Args:
            other: The complex number to divide by.

        Returns:
            A new ComplexNumber containing the quotient, or NotImplemented if
            other is not a ComplexNumber.

        Raises:
            ZeroDivisionError: If both parts of other are zero.
        """
        if not isinstance(other, ComplexNumber):
            return NotImplemented  # eventually TypeError

        if other.real == 0 and other.imaginary == 0:
            raise ZeroDivisionError("Can not divide by zero!")

        real = (self.real * other.real + self.imaginary * other.imaginary) / (
            other.real**2 + other.imaginary**2
        )
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / (
            other.real**2 + other.imaginary**2
        )
        return ComplexNumber(real, imaginary)

    def __eq__(self, other: ComplexNumber) -> bool | NotImplementedType:
        """Compare the real and imaginary parts of two complex numbers.

        Args:
            other: The complex number to compare with.

        Returns:
            True if both parts are equal, otherwise False. Returns NotImplemented
            if other is not a ComplexNumber.
        """
        if not isinstance(other, ComplexNumber):
            return NotImplemented  # eventually False

        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self) -> str:
        """Return a string representation of the complex number.

        Returns:
            The complex number as text, omitting parts that are zero, or "0" if
            both parts are zero.
        """
        # real = 0 and imaginary = 0: "0"
        # real = 0 and imaginary != 0: "xi" or "-xi" (x is placeholder)
        if self.real == 0:
            return "0" if self.imaginary == 0 else f"{self.imaginary}i"

        # real != 0 and imaginary = 0: "x" (x is placeholder)
        if self.imaginary == 0:
            return str(self.real)

        operator = "+" if self.imaginary > 0 else "-"

        # real != 0 and imaginary != 0: "x + xi" or "x - xi" or "-x + xi" or "-x - xi"
        return f"{self.real} {operator} {abs(self.imaginary)}i"


def complex_number_sum(complex_numbers: list[ComplexNumber]) -> ComplexNumber:
    """Calculate the sum of the complex numbers in a list.

    Args:
        complex_numbers: List containing complex numbers.

    Returns:
        A new ComplexNumber containing the sum, or a complex number with both
        parts set to zero if the list is empty.
    """
    return ComplexNumber(
        sum([number.real for number in complex_numbers]),
        sum([number.imaginary for number in complex_numbers]),
    )
