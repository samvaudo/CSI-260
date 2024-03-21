"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""


class LibraryItem:
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
        return f'{self.name}\n{self.isbn}\n{self.type}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item String contains only the name of the item and the type of
        the item I.E. Moby Dick - eBook All subclasses must provide a to_short_string method"""
        return f'{self.name} - {self.isbn}'


class Book(LibraryItem):
    typeof = 'book'

    def __init__(self, name, isbn, numpages, tags=None):
        self.numpages = numpages
        self.typeof = Book.typeof
        LibraryItem.__init__(name, isbn, tags)

    def __str__(self):
        return LibraryItem.__str__() + f'\n{", with ".join(self.numpages)}" pages" '

    def getType(self):
        return self.typeof


class audioBook(LibraryItem):
    typeof = 'audiobook'

    def __init__(self, name, isbn, playtime, tags=None):
        self.playtime = playtime
        self.typeof = audioBook.typeof
        LibraryItem.__init__(name, isbn, tags)

    def getType(self):
        return self.typeof

    def __str__(self):
        return LibraryItem.__str__() + f'\n{", with ".join(self.playtime)}" minutes of playtime" '


class computer(LibraryItem):
    typeof = 'computer'

    def __init__(self, name, isbn, computername, tags=None):
        self.computername = computername
        self.typeof = audioBook.typeof
        LibraryItem.__init__(name, isbn, tags)

    def getType(self):
        return self.typeof

    def __str__(self):
        return f'{"Name:".join(self.computername)}' + LibraryItem.__str__()


class Catalog:
    _collection = []

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls._collection

    @classmethod
    def add_libraryItems(cls, items):
        cls._collection = cls._collection + [item for item in items]

    @classmethod
    def delete_libraryItems(cls, items):
        cls._collection = [item for item in cls._collection if item not in items]

    @classmethod
    def search_for_item(cls, filter_text, typeof='all'):
        if type == 'all':
            return [item for item in cls._collection if item.match(filter_text)]
        else:
            return [item for item in cls._collection if item.match(filter_text) and item.getType == typeof]

