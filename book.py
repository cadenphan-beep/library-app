class Book:
    def __init__(self, title, author, isbn, genre):
        # Store the book's basic info as instance variables
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        
        # Track whether this book is currently checked out
        # Starts as False because all books are available when first added
        self.is_checked_out = False
        
        # Tracks which member has this book — None means nobody has it
        self.checked_out_by = None

    def __repr__(self):
        # Build a human-readable status string for display
        status = "Checked out" if self.is_checked_out else "Available"
        
        # Returns a clean string whenever this object is printed
        return f"'{self.title}' by {self.author} — {status}"
