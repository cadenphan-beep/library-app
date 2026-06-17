class Member:
    def __init__(self, name, member_id):
        # Store the member's name and unique ID
        self.name = name
        self.member_id = member_id
        
        # List of ISBNs for books this member currently has checked out
        # Starts empty because new members haven't borrowed anything yet
        # We store ISBNs rather than Book objects so we have a simple
        # unique identifier to work with across the system
        self.borrowed_books = []

    def __repr__(self):
        # Returns a clean string whenever this object is printed
        return f"Member({self.name}, ID: {self.member_id})"
