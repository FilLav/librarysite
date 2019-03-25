# find and eradicate CHANGEME

from bottle import get, post, install, run, template, static_file, request
from bottle_sqlite import SQLitePlugin

# run dbsetup.py (which is in another folder)
import sys
sys.path.insert(0, 'migrations/initial')
import dbsetup
dbsetup

install(SQLitePlugin(dbfile='migrations/initial/up.sql'))

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
def doquicksearch(db):
    search_query = request.forms.get('quicksearchbox')
    comparison_string = f'%{search_query}%'
    results = db.execute("""SELECT id, title, author, imgsrc, is_available from books WHERE title LIKE ?""", (comparison_string,)).fetchall()
    return template('visitorhome',search_results=results)

# action when doing a refined search
@post('/frontend/visitorsearch/search')
def dorefinedsearch(db):
    search_title = request.forms.get('refinedsearchtitle')
    compare_title = f'%{search_title}%'

    search_authors = request.forms.get('refinedsearchauthors')
    compare_authors = f'%{search_authors}%'

    search_isbn = request.forms.get('refinedsearchisbn')
    match_isbn = f'%{search_isbn}%'

    search_genre = request.forms.get('refinedsearchgenre')
    match_genre = f'%{search_genre}%'

    # CHANGEME: presently doesn't exist. Update alongside corresponding section in visitorsearch.tpl
    # search_keyword = request.forms.get('refinedsearchkeyword')
    # compare_keyword = f'%{search_keyword}%'

    # results will try to match both title and author. Leave 'genre' blank for general results.
    # CHANGEME: Actually I want isbn to override everything (if you search by it, that should be the first result, if not the only one).
    # The current setup doesn't do this... at all.
    results = db.execute("""SELECT id, title, author, isbn, imgsrc, genre, is_available from books
                        WHERE title LIKE ? AND author LIKE ? AND genre LIKE ? OR isbn =?""",
                        (compare_title, compare_authors, match_genre, match_isbn)).fetchall()

    return template('visitorsearch',search_results=results) # this template doesn't yet exist

# action when Borrowing a book (but I don't yet know how to incorporate userid here... ? CHANGEME)
@post('/frontend/visitorhome/borrow/<bookid>')
def borrowbook(bookid, userid):
    db.execute("""INSERT INTO loans (book_id, borrower_id, borrowed_on, borrowing_duration, is_returned) 
                    VALUES (?,?,?,?,0);
                    UPDATE books
                    SET available = 0 WHERE id = bookid;""",
                    (bookid, userid, CHANGEME, CHANGEME)) # need "today's date" and a fixed duration
    
# the 'browse' page for genre is currently a bit of a misnomer. If you want to truly browse a genre, you can do so in the search
# page; this generates 3 random books of the genre each time it's run.
@post('/frontend/browse/genre/<genre>')
def browsegenre(genre):
    db.execute("""SELECT * FROM table WHERE id IN (SELECT id FROM table ORDER BY RANDOM() LIMIT 3)""")

run(host='localhost', port=8080, debug=True)