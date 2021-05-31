class Library:
    def __init__(self, bookslist, name):  # Here, name is the library name
        self.booksList = bookslist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, book, user):
        if book in booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print("Book has been lended. Database updated.")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            print("Apologies! We don't have this book in our library")

    def addBook(self, book):
        if book in booksList:
            print("Book already exists")
        else:
            self.booksList.append(book)
            bookDatabase = open(databaseName, "a")
            bookDatabase.write("\n")
            bookDatabase.write(book)
            print("Book added")

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("Book Returned Successfully")
        else:
            print("The book does not exist in the Book Lending Database")


def main():
    while(True):
        print(
            f"Welcome to the {library.name} library. Following are the options,")
        choice = """ 
        1. Display Books
        2. Lend a Book
        3. Add a Book
        4. Return a Book
        """
        print(choice)

        userInput = input("Press Q to quit and C to continue:")
        if userInput == "C":
            userChoice = int(input("Select an option to continue:"))
            if userChoice == 1:
                library.displayBooks()

            elif userChoice == 2:
                book = input("Enter the name of the book you want to lend:")
                user = input("Enter the name of the user:")
                library.lendBook(book, user)

            elif userChoice == 3:
                book = input("Enter the name of the book you want to add:")
                library.addBook(book)

            elif userChoice == 4:
                book = input("Enter the name of the book you want to return:")
                library.returnBook(book)

            else:
                print("Please choose a valid option")

        elif userInput == "Q":
            break

        else:
            print("Please enter a valid option")


if __name__ == '__main__':
    booksList = []
    databaseName = input("Enter the name of the database file with extension:")
    bookDatabase = open(databaseName, "r")
    for book in bookDatabase:
        booksList.append(book)
    library = Library(booksList, "PythonX")
    main()
