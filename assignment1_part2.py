#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment1-Part2-IS211"""

class Book(object):
    """A class to record books attribute

    Args:
        author (str): Name of Author
        title (str): Name of Book
    """

    author = ''
    title = ''

    def __init__(self, author, title):
        """Constructor for book.
        Args:
            author: Name of Author
            title: Name of Book
        Attributes:
            author: name of author
            title: name of book
        """
        self.author = author
        self.title = title

    def display(self):
        """Displays a book's title and author.
        Args: None
        Returns:
            result(str): Name of Book Tile written by Book Author.
         """

        output = "{}, written by {}"
        result = output.format(self.title, self.author)
        return result

Title1 = Book('John Steinbeck', 'Of Mice and Men')
Title2 = Book('Harper Lee', 'To Kill A Mockingbird')


print Title1.display()
print Title2.display()
