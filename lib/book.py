#!/usr/bin/env python3


class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count
        self._current_page = 1

    @property
    def title(self):
        """The title property"""
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count

    @page_count.setter
    def page_count(self, count):
        """page count must be an integer"""
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Turns a page"""
        if self._current_page < self._page_count:
            self._current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print("You've reached the end of the book.")

    pass
