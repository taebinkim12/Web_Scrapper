from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return "Hello and Welcome!"

@app.route("/test")                                 # "@" --> Decorator: looks for a function to execute underneath
def test():
    return "contact me!"

app.run()