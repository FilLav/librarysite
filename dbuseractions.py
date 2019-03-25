import sqlite3

conn = sqlite3.connect('libdb.db')
c = conn.cursor()

# search for books - quicksearch
def quicksearch(title):
    comparison_string = f'%{quicksearchbox}%'
    results = c.execute("""SELECT title, author, imgsrc from books WHERE title LIKE ?""", comparison_string)

# borrow a book
c.execute("""INSERT INTO loans (book_id, borrower_id, borrowed_on, borrowing_duration, is_returned) 
			            VALUES (?,?,?,?,0);

            UPDATE books
            SET available = 0 WHERE id = ;""",
            (, , , , ))

# edit own details
c.execute("""UPDATE users
            SET first_name = ?, last_name = ? WHERE id = """,
            (, ))