from library_books import library_books
from datetime import datetime, timedelta

# This part helps find a book by its ID (it is case-insensitive)
def find_book_by_id(library_books, book_id):
    book_id = book_id.strip().lower()
    for book in library_books:
        if book["id"].lower() == book_id:
            return book
    return None

# This part helps format one book as a single line of text
def format_book_line(book):
    return f"{book['id']} | {book['title']} by {book['author']} | {book['genre']} | Available: {book['available']}"

# This part helps print a list of books cleanly
def print_books(books):
    if not books:
        print("No books found.")
        return
    for b in books:
        print(format_book_line(b))


# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def view_available_books(library_books):
    """Print all books that are currently available."""
    available_books = [book for book in library_books if book["available"] is True]
    print_books(available_books)


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_books(library_books, term):
    """Return a list of books that match the author or genre (case-insensitive)."""
    term = term.strip().lower()
    results = []

    for book in library_books:
        if term in book["author"].lower() or term in book["genre"].lower():
            results.append(book)

    return results


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book(library_books, book_id):
    """Checkout a book by ID if available, set due date, and increment checkout count."""
    book = find_book_by_id(library_books, book_id)

    if book is None:
        print("Book ID not found.")
        return False
    
    if book["available"] is False:
        print(f"This book is already checked out. Due back on {book['due_date']}.")
        return False
    
    # Perform checkout
    book["available"] = False
    due_date = (datetime.today() + timedelta(weeks=2)).date().isoformat()
    book["due_date"] = due_date
    book["checkouts"] += 1

    print(f"'{book['title']}' has been checked out. Due date: {due_date}.")
    return True    


# -------- User Input --------
def run_menu(library_books):
    while True:
        print("\n--- Library Menu ---")
        print("1. View available books")
        print("2. Search for books by author or genre")
        print("3. Checkout a book")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        # Level 1
        if choice == "1":
            view_available_books(library_books)

        # Level 2
        elif choice == "2":
            term = input("Enter author or genre to search: ")
            results = search_books(library_books, term)
            print_books(results)

        # Level 3
        elif choice == "3":
            book_id = input("Enter the book ID to checkout: ")
            checkout_book(library_books, book_id)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1–4.")

run_menu(library_books)


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
