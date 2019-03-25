# config
database_file = 'migrations/2019-03-25-initial-migration/up.sql'

# database seeding
import sqlite3

conn = sqlite3.connect(database_file)

conn.execute("""CREATE TABLE IF NOT EXISTS books (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                imgsrc TEXT NOT NULL,
                isbn INT NOT NULL,
                genre TEXT,
                is_available BOOLEAN
                );""")

# DELETEME - getting rid of test data before refreshing
conn.execute("""DELETE FROM books""")

# DELETEME - test data inputs
conn.execute("""INSERT INTO books (title, author, imgsrc, isbn, genre, is_available) VALUES
                        ('httyd', 'c cowell', '/static/images/bookish.png', 9781444913989, 'fantasy', 0),
                        ('funny bear', 'a a milne', '/static/images/hunny.png', 8601200488852, 'childrens', 1);""")

conn.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                currency INT NOT NULL,
                fees INT NOT NULL
                 );""")

conn.execute("""CREATE TABLE IF NOT EXISTS loans (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                book_id INT NOT NULL,
                borrower_id INT NOT NULL,
                borrowed_on DATE NOT NULL,
                borrowing_duration INT NOT NULL,
                loan_status INT NOT NULL,
                    -- 0 = reserved, 1 = physically loaned, 2 = returned
                FOREIGN KEY (book_id) REFERENCES books(id),
                FOREIGN KEY (borrower_id) REFERENCES users(id)
                  );""")

conn.commit()