#!/usr/bin/python3
"""This module defines a Square class with getter, setter, and area."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the side of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
