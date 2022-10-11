from flask import Flask

def make_bold(function):
    #print(f"Output: {function()}")
    def bold():
        return f"<b> {function()} </b>"
    return bold
def make_underline(function):
    #print(f"Output: {function()}")
    def underline():
        return f"<u> {function()} </u>"
    return underline
def make_italics(function):
    #print(f"Output: {function()}")
    def italics():
        return f"<i> {function()} </i>"
    return italics
app = Flask(__name__) # flask needs to check that the current file is the correct one 

@app.route('/')
@make_bold
@make_underline
@make_italics
def hello_world(): 
    return 'Hello, Worldy!'

@app.route('/bye')
def say_bye():
    return 'Bye Bye!'

#adding variables with <variable>
@app.route('/username/<name>/<int:number>')
def greet(name,number):
    return f"Hello {name}, you are {number} years old!"

#e.g. enter http://127.0.0.1:5000/username/stefan/2

app.run()    