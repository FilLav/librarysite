from bottle import get, run

@get('/greet/<name>')
def greet(name):
    return f"Message in a bottle for {name}!"

run(host='localhost', port=8080, debug=True)