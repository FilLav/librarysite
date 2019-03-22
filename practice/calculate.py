from bottle import get, install, run, template, static_file
from bottle_sqlite import SQLitePlugin
install(SQLitePlugin(dbfile='cubes'))

@get('/calculate/<num>')
@get('/calculate')
def calculate(db, num=2):
    result = db.execute('select ? * ? * ?', (num, num, num)).fetchone()[0]
    return f'{num} cubed is {result}'

run(host='localhost', port=8080, debug=True)