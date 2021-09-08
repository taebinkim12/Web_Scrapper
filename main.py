from flask import Flask, render_template, request, redirect, send_file
from Scrapper import get_jobs
from export import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test")                                     # "@" --> Decorator: looks for a function to execute underneath
def test():
    return "Testing!"

@app.route("/report")
def report():
    word = (request.args.get('word'))                   # Comes as Dictionary
    if word:
        word = word.lower()
        exisitingJobs = db.get(word)
        if exisitingJobs:
            jobs = exisitingJobs
        else:
           jobs = get_jobs(word)                        # Scrapper
           db[word] = jobs     
    else:
        return redirect("/")

    return render_template("report.html", searchBy= word, resultNumber = len(jobs), jobs = jobs)

# @app.route("/<username>")                             # Dynamic URLs
# def username(username):
#     return f"Hello your name is {username}"

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:                                                 # Consequence of Exception
        return redirect("/")

app.run()