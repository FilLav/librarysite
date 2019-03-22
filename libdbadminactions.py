import sqlite3

conn = sqlite3.connect('libdb.db')
c = conn.cursor()

# add to books
c.execute("""INSERT INTO books (title, author, imgsrc, isbn, genre, is_available) 
                        VALUES (?,?,?,?,?, 1);""",
                        (, , , , ))

# edit a book
c.execute("""UPDATE books
            SET title = ?, author = ?, imgsrc = ?, isbn = ?, genre = ?, is_available = ? WHERE id = """,
            (, , , , , ))

# add to users. note that I don't think it makes sense for admin to be able to edit user photo -
    # it isn't that important anyway, so I leave it out here.
c.execute("""INSERT INTO users (first_name, last_name, currency, fees)
                        VALUES (?,?, 0, 0);""",
                        (, , ))

# edit a user
c.execute("""UPDATE users
            SET first_name = ?, last_name = ?, """)