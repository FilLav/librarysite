# find and eradicate CHANGEME

from bottle import get, post, install, run, template, static_file, request
from bottle_sqlite import SQLitePlugin
install(SQLitePlugin(dbfile='libdb.db'))

# load static /visitorhome page
@get('/frontend/visitorhome')
def visitorhome(db):
    return template('visitorhome')

# load static /visitorsearch page
@get('/frontend/visitorsearch')
def visitorsearch(db):
    return template('visitorsearch')

# to add images and stuff I think?
@get('/static/<file:path>')
def serve_static(file):
    return static_file(file, root='./static')

# action when doing a quicksearch from the front page
@post('/frontend/visitorhome/quicksearch')
def search(db):
    search_query = request.forms.get('quicksearchbox')
    comparison_string = f'%{search_query}%'
    results = db.execute("""SELECT id, title, author, imgsrc, is_available from books WHERE title LIKE ?""", (comparison_string,)).fetchall()
    return template('visitorhome',search_results=results)

# action when doing a refined search
@post('/frontend/visitorsearch/search')
def search(db):
    search_title = request.forms.get('refinedsearchtitle')
    compare_title = f'%{search_title}%'

    search_authors = request.forms.get('refinedsearchauthors')
    compare_authors = f'%{search_authors}%'

    search_isbn = request.forms.get('refinedsearchisbn')

    search_genre = request.forms.get('refinedsearchgenre')

    # presently doesn't exist. Update alongside corresponding section in visitorsearch.tpl
    # search_keyword = request.forms.get('refinedsearchkeyword')
    # f'%{search_keyword}%'

    results = db.execute("""SELECT id, title, author, isbn, imgsrc, genre, is_available from books
                        WHERE title LIKE ?, author LIKE ?, isbn=?, genre=?""",
                        (compare_title, compare_authors, search_isbn, search_genre))

    return template('CHANGEME',search_results=results) # this template doesn't yet exist



# action when Borrowing a book (but I don't yet know how to incorporate userid here... ? NEED TO ADD THAT)
@post('/frontend/visitorhome/borrow/<bookid>')
def borrowbook(bookid, userid):
    db.execute("""INSERT INTO loans (book_id, borrower_id, borrowed_on, borrowing_duration, is_returned) 
                    VALUES (?,?,?,?,0);
                    UPDATE books
                    SET available = 0 WHERE id = bookid;""",
                    (bookid, userid, CHANGEME, CHANGEME)) # need "today's date" and a fixed duration
    


run(host='localhost', port=8080, debug=True)