books = {}

while True:
    print("\n" + "=" * 40)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")

        if book_id in books:
            print("Book ID already exists.")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            books[book_id] = {
                "Title": title,
                "Author": author,
                "Issued": False
            }

            print("Book added successfully!")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            print("\nBook List")
            for book_id, details in books.items():
                status = "Issued" if details["Issued"] else "Available"

                print(f"\nBook ID : {book_id}")
                print(f"Title   : {details['Title']}")
                print(f"Author  : {details['Author']}")
                print(f"Status  : {status}")

    elif choice == "3":
        book_id = input("Enter Book ID to issue: ")

        if book_id in books:
            if books[book_id]["Issued"]:
                print("Book is already issued.")
            else:
                books[book_id]["Issued"] = True
                print("Book issued successfully!")
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Enter Book ID to return: ")

        if book_id in books:
            if books[book_id]["Issued"]:
                books[book_id]["Issued"] = False
                print("Book returned successfully!")
            else:
                print("Book is already available.")
        else:
            print("Book not found.")

    elif choice == "5":
        book_id = input("Enter Book ID to remove: ")

        if book_id in books:
            del books[book_id]
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")