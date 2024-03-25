# Author: Samuel Vaudo
# Class: CSI-260-01
# Certification of Authenticity:
# I certify that this is entirely my own work, except where I have given fully documented
# references to the work of others. I understand the definition and consequences of
# plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
# assessing this assignment reproduce this assignment and provide a copy to another member
# of academic staff and / or communicate a copy of this assignment to a plagiarism checking
# service(which may then retain a copy of this assignment on its database for the purpose
# of future plagiarism checking)
"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""

from abc import ABC, abstractmethod
import pickle

class LibraryItem(ABC):
    """Base class for all items stored in a library catalog

        Provides a simple LibraryItem with only a few attributes

    """

    def __init__(self, name, isbn, tags=None):
        """Initialize a LibraryItem

        :param name: (string) Name of item
        :param isbn: (string) ISBN for the item
        :param tags: (list) List of CategoryTags
        """
        self.name = name
        self.isbn = isbn
        if tags:
            self.tags = tags
            for tag in tags:
                CategoryTag(tag)
        else:
            self.tags = list()

    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text match should be case-insensitive and should
        search all attributes of the class. Depending on the attribute, match requires an exact match or partial
        match. match needs to be redefined for any subclasses. Please see the note/notebook case study from Chapter 2
        as an example of how match is designed to work.
        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or filter_text.lower() == self.isbn.lower() or filter_text.lower() in (
            str(tag).lower() for tag in self.tags)

    def __str__(self):
        """Return a well formatted string representation of the item All instance variables are included. All
        subclasses must provide a __str__ method"""
        return f'{"Name:" + self.name}\n{"ISBN:" + str(self.isbn)}\n{"Type:" + self.typeof}\n{"With the following tags:, ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item String contains only the name of the item and the type of
        the item I.E. Moby Dick - eBook All subclasses must provide a to_short_string method"""
        return f'{self.name} - {self.isbn}'

    @abstractmethod
    def getType(self):
        """
        Abstract method that includes subclass function
        :return: None
        """
        pass


class Book(LibraryItem):
    typeof = 'book'

    def __init__(self, name, isbn, numpages, tags=None):
        """
        Initalized a book object
        :param name: Name of book
        :param isbn: ISBN of book
        :param numpages: Number of pages in the book (typically an integer)
        :param tags: Tags associated with the book
        """
        self.numpages = numpages
        self.typeof = Book.typeof
        super().__init__(name, isbn, tags)

    def __str__(self):
        return super().__str__() + f'\n{"With " + str(self.numpages) + " pages"}'

    def getType(self):
        return self.typeof


class audioBook(LibraryItem):
    typeof = 'audiobook'

    def __init__(self, name, isbn, playtime, tags=None):
        """
        Initalized an audiobook object
        :param name: Name of audiobook
        :param isbn: ISBN of audiobook
        :param playtime: playtime (in minutes)
        :param tags: Tags associated
        """
        self.playtime = playtime
        self.typeof = audioBook.typeof
        super().__init__(name, isbn, tags)

    def getType(self):
        return self.typeof

    def __str__(self):
        return super().__str__() + f'\n{"With" + str(self.playtime)}" minutes of playtime" '


class computer(LibraryItem):
    typeof = 'computer'

    def __init__(self, name, isbn, computername, tags=None):
        """
        Initalized a computer object
        :param name: Name of computer (different than computername)
        :param isbn: ISBN of computer (can leave as 0)
        :param computername: name of computer (number format)
        :param tags: Tags associated
        """
        self.computername = computername
        self.typeof = computer.typeof
        super().__init__(name, isbn, tags)

    def getType(self):
        return self.typeof

    def __str__(self):
        return f'{"Computer Name:" + str(self.computername)}\n' + super().__str__()


class CategoryTag:
    _list_tags = []

    def __init__(self, name):
        """
        Initalizes a CategoryTag object
        :param name: Name of tag
        """
        self.name = name
        namesame = False
        for item in CategoryTag._list_tags:
            if str(item) == name:
                namesame = True
        if namesame:
            pass
        else:
            CategoryTag._list_tags.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def all_category_tags(cls):
        """
        Gets all tags stored in the class
        :return: All tags in a string format
        """
        return [f'{tag}\n' for tag in cls._list_tags]


class Catalog:
    _collection = []

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @classmethod
    def get_all(cls):
        """
        Returns entire collection
        :return: entire collection as a list
        """
        return cls._collection

    @classmethod
    def add_libraryItems(cls, items):
        """
        Adds items to catalog
        :param items: LibraryItems (in list) to be added
        :return: None
        """
        cls._collection = cls._collection + [item for item in items]

    @classmethod
    def delete_libraryItems(cls, items):
        """
        Deletes selected items in a list
        :param items: LibraryItems (in list) to be deleted
        :return: None
        """
        cls._collection = [item for item in cls._collection if item not in items]

    @classmethod
    def search_for_item(cls, filter_text, typeof='all'):
        """
        Searches all of the catalog for an item
        :param filter_text: Query text to filter with
        :param typeof: Type of item to search for
        :return: All matching items
        """
        if type == 'all':
            return [item for item in cls._collection if item.match(filter_text)]
        else:
            return [item for item in cls._collection if item.match(filter_text) and item.getType == typeof]

    @classmethod
    def save_2_pkl(cls,filename):
        """
        Saves collection to a pkl file
        :param filename: Name of file to save to
        :return: Boolean of save success
        """
        try:
            with open(filename+'.pickle', 'wb') as f:
                pickle.dump(cls._collection,f)
                return True
        except:
            return False

    @classmethod
    def import_from_pkl(cls, filename):
        """
        Imports .pkl file to collection
        :param filename: Name of file to import to
        :return: Boolean of import success
        """
        try:
            with open(filename+'.pickle', 'rb') as f:
                cls._collection= pickle.load(f)
                return True
        except:
            return False




