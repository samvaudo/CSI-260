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



from library import *




def display_menu():
    print("""\
Library Catalog Menu

1. Search catalog
2. Print the entire catalog
3. Add item to catalog
4. Remove item from catalog
5. Export Collection
6. Import collection from file
7. Quit
""")


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.choices = {
            "1": self.search,
            "2": self.print_all,
            "3": self.add_item,
            "4": self.remove_item,
            "5": self.export_all,
            "6": self.import_all,
            "7": self.quit,
        }

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def search(self):
        choice1 = input("What type do you want to filter for? (book, audiobook, computer or all): ")
        query = input("What is the query that you want to search for?: ")
        results = Catalog.search_for_item(query, choice1)
        if not results:
            print("No results!")
        else:
            for item in results:
                print(item)

    def print_all(self):
        for item in Catalog.get_all():
            print(item)

    def add_item(self):
        name = input("What is the name of this item?:")
        isbn = input("What is the ISBN of this item?:")
        tags = 'a'
        tagslist = []
        while tags != '':
            tags = input("Any tags that you want to add? (press enter to skip): ")
            if tags != '':
                tagslist.append(tags)
            else:
                print("Ok! Done.")
        if not tagslist:
            tagslist = None

        choice2 = input("What type of item would you like to add?: (book, audiobook, or computer) ")
        newitem = None
        if choice2 == 'book':
            pagenum = int(input("How many pages does this book have? (Integer)"))
            newitem = Book(name, isbn, pagenum, tagslist)
        elif choice2 == 'audiobook':
            playtime = int(input("How long is this audiobook?: (Minutes)"))
            newitem = audioBook(name, isbn, playtime, tagslist)
        else:
            compname = input("What is this computer's name?: ")
            newitem = computer(name, isbn, compname, tagslist)
        confirm = input(str(newitem) + "\nIs this the item that you wish to add?: (y/n)")
        if confirm.lower() == "y":
            Catalog.add_libraryItems([newitem])
        else:
            print("canceling process....")

    def remove_item(self):
        isbn = input("What is the isbn of the item that you want to delete?: ")
        removed = Catalog.search_for_item(isbn)
        if removed != []:
            for i in range(len(removed)):
                print(i, removed[i])

            index = int(input("What index should be removed?"))
            if index in range(len(removed)):
                Catalog.delete_libraryItems(removed[index])
            else:
                print("Not a valid index, resetting....")
        else:
            print("No results, try again...")

    def export_all(self):
        name = input("What filename should the catalog be saved to? (no .pkl suffix needed):")
        result = Catalog.save_2_pkl(name)
        if result:
            print("Saved!")
        else:
            print("An error has occurred, canceling...")

    def import_all(self):
        name = input("What filename should the catalog be imported from? (no .pkl suffix needed):")
        result = Catalog.import_from_pkl(name)
        if result:
            print("Successfully Imported!")
        else:
            print("An error has occurred, canceling...")

    def quit(self):
        print("Goodbye!")
        quit()


if __name__ == "__main__":
    Menu().run()
