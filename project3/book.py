class Library:
    def __init__(self):
        self.books = {
            "Python Basics": {"available": True, "borrowed": 0},
            "Java Programming": {"available": True, "borrowed": 0},
            "Data Structures": {"available": True, "borrowed": 0},
            "Machine Learning": {"available": True, "borrowed": 0},
            "Web Development": {"available": True, "borrowed": 0}
        }

    def show_books(self):
        print("\nLibrary Books:")
        for book, info in self.books.items():
            status = "Available" if info["available"] else "Not Available"
            print(f"{book} - {status}")

    def borrow_book(self):
        name = input("Enter book name to borrow: ")
        if name in self.books:
            if self.books[name]["available"]:
                self.books[name]["available"] = False
                self.books[name]["borrowed"] += 1
                print("Book borrowed successfully!")
            else:
                print("Book not available.")
        else:
            print("Book not found.")

    def return_book(self):
        name = input("Enter book name to return: ")
        if name in self.books:
            self.books[name]["available"] = True
            print("Book returned successfully!")
        else:
            print("Book not found.")

    def popular_books(self):
        print("\nPopular Books:")
        sorted_books = sorted(self.books.items(), key=lambda x: x[1]["borrowed"], reverse=True)
        for book, info in sorted_books:
            print(f"{book} - Borrowed {info['borrowed']} times")


library = Library()

while True:
    print("\n**** Library Menu ****")
    print("1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Popular Books")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.show_books()
    elif choice == "2":
        library.borrow_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        library.popular_books()
    elif choice == "5":
        print("Exiting Library System")
        break
    else:
        print("Invalid choice")