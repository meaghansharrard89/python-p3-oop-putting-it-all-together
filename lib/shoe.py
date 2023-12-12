#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size, cobble=None):
        self._brand = brand
        self._size = size
        self._condition = "New"

    @property
    def brand(self):
        """The brand property"""
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        """The size property"""
        return self._size

    @size.setter
    def size(self, size):
        """size must be an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        """Repairs shoe and sets cobble to 'New'"""
        print("Your shoe is as good as new!")
        self._condition = "New"

    @property
    def condition(self):
        """The condition property"""
        return self._condition

    pass
