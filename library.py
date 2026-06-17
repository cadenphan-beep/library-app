from book import Book
from member import Member

class Library:
    def __init__(self):
        # Store books as a dict keyed by ISBN — makes lookup O(1)
        # instead of searching through a list every time
        self.books = {}
        
        # Store members as a dict keyed by member ID — same reason
        self.members = {}
        
        # Simple counter to auto-generate unique member IDs
        self.next_member_id = 1

    # ─── Book management ───────────────────────────────────────────

    def add_book(self, title, author, isbn, genre):
        # Don't allow duplicate ISBNs — each book must be unique
        if isbn in self.books:
            print(f"A book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = Book(title, author, isbn, genre)
        print(f"Added: '{title}' by {author}")

    def remove_book(self, isbn):
        # Can't remove a book that doesn't exist
        if isbn not in self.books:
            print("Book not found.")
            return
        
        # Can't remove a book that's currently checked out
        if self.books[isbn].is_checked_out:
            print("Cannot remove a book that is currently checked out.")
            return
        
        removed = self.books.pop(isbn)
        print(f"Removed: '{removed.title}'")

    # ─── Member management ─────────────────────────────────────────

    def register_member(self, name):
        # Create a new member with an auto-generated ID
        member_id = self.next_member_id
        self.members[member_id] = Member(name, member_id)
        self.next_member_id += 1
        print(f"Registered '{name}' with member ID {member_id}")
        return member_id

    def get_member(self, member_id):
        # Helper to safely retrieve a member — returns None if not found
        return self.members.get(member_id)

    # ─── Checkout and return ───────────────────────────────────────

    def checkout_book(self, isbn, member_id):
        # Validate the book exists
        if isbn not in self.books:
            print("Book not found.")
            return
        
        # Validate the member exists
        if member_id not in self.members:
            print("Member not found.")
            return
        
        book = self.books[isbn]
        member = self.members[member_id]

        # Can't check out a book that's already checked out
        if book.is_checked_out:
            print(f"'{book.title}' is already checked out.")
            return

        # Update the book's state
        book.is_checked_out = True
        book.checked_out_by = member_id

        # Add the ISBN to the member's borrowed list
        member.borrowed_books.append(isbn)

        print(f"'{book.title}' checked out to {member.name}.")

    def return_book(self, isbn, member_id):
        # Validate the book exists
        if isbn not in self.books:
            print("Book not found.")
            return
        
        # Validate the member exists
        if member_id not in self.members:
            print("Member not found.")
            return

        book = self.books[isbn]
        member = self.members[member_id]

        # Make sure this book is actually checked out by this member
        if not book.is_checked_out or book.checked_out_by != member_id:
            print(f"'{book.title}' was not checked out by {member.name}.")
            return

        # Reset the book's state
        book.is_checked_out = False
        book.checked_out_by = None

        # Remove the ISBN from the member's borrowed list
        member.borrowed_books.remove(isbn)

        print(f"'{book.title}' returned by {member.name}.")

    # ─── Search ────────────────────────────────────────────────────

    def search(self, query):
        query = query.lower()
        
        # Check every book to see if query matches title or author
        results = [
            book for book in self.books.values()
            if query in book.title.lower() or query in book.author.lower()
        ]

        if not results:
            print("No books found.")
            return

        print(f"\n{len(results)} result(s) found:")
        for book in results:
            print(f"  {book}")

    # ─── Display ───────────────────────────────────────────────────

    def show_available_books(self):
        # Filter to only books that are not checked out
        available = [b for b in self.books.values() if not b.is_checked_out]
        
        if not available:
            print("No books currently available.")
            return

        print(f"\nAvailable books ({len(available)}):")
        for book in available:
            print(f"  {book}")

    def show_member_books(self, member_id):
        if member_id not in self.members:
            print("Member not found.")
            return

        member = self.members[member_id]

        if not member.borrowed_books:
            print(f"{member.name} has no books checked out.")
            return

        print(f"\n{member.name}'s checked out books:")
        for isbn in member.borrowed_books:
            print(f"  {self.books[isbn]}")
