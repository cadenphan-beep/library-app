from library import Library

def print_menu():
    print("\n─────────────────────────────")
    print("       Library System        ")
    print("─────────────────────────────")
    print("1. Show available books")
    print("2. Search books")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. My books")
    print("6. Register new member")
    print("7. Add a book")
    print("8. Remove a book")
    print("9. Exit")
    print("─────────────────────────────")

def get_int(prompt):
    # Safely get an integer from the user — handles bad input without crashing
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
    library = Library()

    # Seed some books so there's something to work with immediately
    library.add_book("The Pragmatic Programmer", "David Thomas", "978-0135957059", "Technology")
    library.add_book("Clean Code", "Robert Martin", "978-0132350884", "Technology")
    library.add_book("Dune", "Frank Herbert", "978-0441013593", "Science Fiction")
    library.add_book("1984", "George Orwell", "978-0451524935", "Fiction")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", "Fiction")

    # Seed a member so you can test checkout immediately
    library.register_member("Caden")

    print("\nWelcome to the Library System!")

    while True:
        print_menu()
        choice = get_int("Choose an option: ")

        if choice is None:
            continue

        # ── 1. Show available books ──────────────────────────────
        elif choice == 1:
            library.show_available_books()

        # ── 2. Search ────────────────────────────────────────────
        elif choice == 2:
            query = input("Search by title or author: ").strip()
            if query:
                library.search(query)
            else:
                print("Please enter a search term.")

        # ── 3. Check out a book ──────────────────────────────────
        elif choice == 3:
            isbn = input("Enter the book ISBN: ").strip()
            member_id = get_int("Enter your member ID: ")
            if member_id:
                library.checkout_book(isbn, member_id)

        # ── 4. Return a book ─────────────────────────────────────
        elif choice == 4:
            isbn = input("Enter the book ISBN: ").strip()
            member_id = get_int("Enter your member ID: ")
            if member_id:
                library.return_book(isbn, member_id)

        # ── 5. My books ──────────────────────────────────────────
        elif choice == 5:
            member_id = get_int("Enter your member ID: ")
            if member_id:
                library.show_member_books(member_id)

        # ── 6. Register new member ───────────────────────────────
        elif choice == 6:
            name = input("Enter your name: ").strip()
            if name:
                library.register_member(name)
            else:
                print("Please enter a name.")

        # ── 7. Add a book ────────────────────────────────────────
        elif choice == 7:
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            genre = input("Genre: ").strip()
            if title and author and isbn and genre:
                library.add_book(title, author, isbn, genre)
            else:
                print("All fields are required.")

        # ── 8. Remove a book ─────────────────────────────────────
        elif choice == 8:
            isbn = input("Enter the book ISBN: ").strip()
            library.remove_book(isbn)

        # ── 9. Exit ──────────────────────────────────────────────
        elif choice == 9:
            print("\nGoodbye!")
            break

        else:
            print("Invalid option, please choose 1-9.")

if __name__ == '__main__':
    main()
