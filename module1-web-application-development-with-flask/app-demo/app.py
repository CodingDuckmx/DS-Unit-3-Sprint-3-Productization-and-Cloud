from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print('Visited the Hello Page')
    return "Hello World!"

@app.route("/about")
def about():
    print('Visited the About Page')
    return "About me!"