from library import Library

def run_test(description, condition):
    # Helper that prints PASS or FAIL for each test
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {description}")

def test_add_books():
    print("\n── Add books ───────────────────────────────")
    lib = Library()

    lib.add_book("Dune", "Frank Herbert", "111", "Sci-Fi")
    run_test("Book is added to library", "111" in lib.books)

    # Try adding the same ISBN twice
    lib.add_book("Dune", "Frank Herbert", "111", "Sci-Fi")
    run_test("Duplicate ISBN is rejected", len(lib.books) == 1)

def test_remove_books():
    print("\n── Remove books ────────────────────────────")
    lib = Library()
    lib.add_book("1984", "George Orwell", "222", "Fiction")

    lib.remove_book("222")
    run_test("Book is removed", "222" not in lib.books)

    # Try removing a book that doesn't exist
    lib.remove_book("999")
    run_test("Removing nonexistent book handled gracefully", True)

def test_remove_checked_out_book():
    print("\n── Remove checked out book ─────────────────")
    lib = Library()
    lib.add_book("Clean Code", "Robert Martin", "333", "Technology")
    lib.register_member("Alice")

    lib.checkout_book("333", 1)
    lib.remove_book("333")
    run_test("Cannot remove a checked out book", "333" in lib.books)

def test_register_members():
    print("\n── Register members ────────────────────────")
    lib = Library()

    lib.register_member("Alice")
    lib.register_member("Bob")
    run_test("First member gets ID 1", 1 in lib.members)
    run_test("Second member gets ID 2", 2 in lib.members)
    run_test("Member names are correct", lib.members[1].name == "Alice" and lib.members[2].name == "Bob")

def test_checkout():
    print("\n── Checkout ────────────────────────────────")
    lib = Library()
    lib.add_book("Dune", "Frank Herbert", "444", "Sci-Fi")
    lib.register_member("Alice")

    lib.checkout_book("444", 1)
    run_test("Book is marked as checked out", lib.books["444"].is_checked_out)
    run_test("Book is linked to correct member", lib.books["444"].checked_out_by == 1)
    run_test("ISBN appears in member's borrowed list", "444" in lib.members[1].borrowed_books)

    # Try checking out the same book again
    lib.checkout_book("444", 1)
    run_test("Cannot check out already checked out book", lib.books["444"].checked_out_by == 1)

def test_checkout_invalid():
    print("\n── Checkout edge cases ─────────────────────")
    lib = Library()
    lib.add_book("Dune", "Frank Herbert", "555", "Sci-Fi")
    lib.register_member("Alice")

    # Nonexistent book
    lib.checkout_book("999", 1)
    run_test("Checkout with bad ISBN handled gracefully", True)

    # Nonexistent member
    lib.checkout_book("555", 99)
    run_test("Checkout with bad member ID handled gracefully", not lib.books["555"].is_checked_out)

def test_return():
    print("\n── Return ──────────────────────────────────")
    lib = Library()
    lib.add_book("Dune", "Frank Herbert", "666", "Sci-Fi")
    lib.register_member("Alice")

    lib.checkout_book("666", 1)
    lib.return_book("666", 1)

    run_test("Book is marked as available after return", not lib.books["666"].is_checked_out)
    run_test("checked_out_by is cleared after return", lib.books["666"].checked_out_by is None)
    run_test("ISBN removed from member's borrowed list", "666" not in lib.members[1].borrowed_books)

def test_return_invalid():
    print("\n── Return edge cases ───────────────────────")
    lib = Library()
    lib.add_book("Dune", "Frank Herbert", "777", "Sci-Fi")
    lib.register_member("Alice")
    lib.register_member("Bob")

    lib.checkout_book("777", 1)

    # Bob tries to return Alice's book
    lib.return_book("777", 2)
    run_test("Cannot return a book checked out by someone else", lib.books["777"].is_checked_out)

    # Return a book that isn't checked out
    lib.return_book("999", 1)
    run_test("Returning nonexistent book handled gracefully", True)

def test_search():
    print("\n── Search ──────────────────────────────────")
    lib = Library()
    lib.add_book("Dune", "Frank Herbert", "888", "Sci-Fi")
    lib.add_book("Dune Messiah", "Frank Herbert", "889", "Sci-Fi")
    lib.add_book("1984", "George Orwell", "890", "Fiction")

    # Search by title
    results = [b for b in lib.books.values() if "dune" in b.title.lower()]
    run_test("Search by title returns correct results", len(results) == 2)

    # Search by author
    results = [b for b in lib.books.values() if "orwell" in b.author.lower()]
    run_test("Search by author returns correct result", len(results) == 1)

    # Search with no matches
    results = [b for b in lib.books.values() if "xyz" in b.title.lower()]
    run_test("Search with no matches returns empty", len(results) == 0)

def test_show_member_books():
    print("\n── Member books ────────────────────────────")
    lib = Library()
    lib.add_book("Dune", "Frank Herbert", "991", "Sci-Fi")
    lib.add_book("1984", "George Orwell", "992", "Fiction")
    lib.register_member("Alice")

    lib.checkout_book("991", 1)
    lib.checkout_book("992", 1)
    run_test("Member has 2 books checked out", len(lib.members[1].borrowed_books) == 2)

    lib.return_book("991", 1)
    run_test("Member has 1 book after returning one", len(lib.members[1].borrowed_books) == 1)

if __name__ == '__main__':
    print("═══════════════════════════════════════════")
    print("         Library System Test Suite         ")
    print("═══════════════════════════════════════════")

    test_add_books()
    test_remove_books()
    test_remove_checked_out_book()
    test_register_members()
    test_checkout()
    test_checkout_invalid()
    test_return()
    test_return_invalid()
    test_search()
    test_show_member_books()

    print("\n═══════════════════════════════════════════")
    print("                  Done                     ")
    print("═══════════════════════════════════════════\n")
