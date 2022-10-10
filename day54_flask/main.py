from flask import Flask
app = Flask(__name__)

@app.route('/') # show me the home page (the root)
def hello_world():
    return 'Hello, Worldy!'

app.run()    