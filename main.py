from flask import Flask, render_template, request, redirect

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test")                                 # "@" --> Decorator: looks for a function to execute underneath
def test():
    return "contact me!"

@app.route("/report")
def report():
    word = (request.args.get('word'))                 # Comes as Dictionary
    if word:
        word = word.lower()
    else:
        return redirect("/")
    return render_template("report.html", searchBy= word)

# @app.route("/<username>")                           # Dynamic URLs
# def username(username):
#     return f"Hello your name is {username}"


app.run()