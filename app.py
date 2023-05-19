from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sightseeing")
def sightseeing():
    return render_template("sightseeing.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/roadrules")
def roadrules():
    return render_template("roadrules.html")

@app.route("/bikingvspublictransport")
def bikingvspublictransport():
    return render_template("bikingvspublictransport.html")





























@app.route("/truegrit")
def truegrit():
    return render_template("truegrit.html")

@app.route("/westsidestory")
def westsidestory():
    return render_template("westsidestory.html")

@app.route("/rental")
def rental():
    return render_template("rental.html")