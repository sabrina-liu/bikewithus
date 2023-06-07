from flask import Flask, request, session, render_template, redirect
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/roadrules")
def roadrules():
    return render_template("roadrules.html")

@app.route("/fivereasons")
def fivereasons():
    return render_template("fivereasons.html")


@app.route("/bikeroute")
def bikeroute():
    return render_template("bikeroute.html")

@app.route("/rental")
def rental():
    return render_template("rental.html")

if __name__ == '__main__':
    app.run(port=3000, debug=True)