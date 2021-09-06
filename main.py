from flask import Flask, render_template, request, redirect
from Scrapper import get_jobs

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test")                                 # "@" --> Decorator: looks for a function to execute underneath
def test():
    return "Testing!"

@app.route("/report")
def report():
    word = (request.args.get('word'))                 # Comes as Dictionary
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect("/")
    return render_template("report.html", searchBy= word)

# @app.route("/<username>")                           # Dynamic URLs
# def username(username):
#     return f"Hello your name is {username}"


app.run()