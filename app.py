from flask import Flask, request, session, render_template, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


# Configure app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Configure flask session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database and database models
db = SQLAlchemy(app)

# Database model for the continuous variable: time spent
class PageView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.String(10))
    page = db.Column(db.String(255))
    time_spent = db.Column(db.Integer)
    start_time = db.Column(db.DateTime)

# Database model for the binary variable: button click
class Button(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.String(10))
    button = db.Column(db.Boolean)

# Create all the tables for the databases
with app.app_context():
    db.create_all()

# Function to log data: this function saves the time spent on the previous page in the database. Unit of time is seconds. 
def log_data():
    try:
        time_spent = (datetime.now() - start_time).total_seconds()

        # First 3 seconds is the threshold to save the time spent in the database. It is to eliminate recording repetitive page requests/reloads. 
        if time_spent > 3:
            page_view = PageView(
                visitor_id = session.get('visitor_id'),
                page = previous_path,
                time_spent = time_spent,
                start_time = start_time)
            db.session.add(page_view)
            db.session.commit()
    except:
        pass

##################################################################################
#
# After Each Request...
#
##################################################################################

# after_request decorator of Flask defines actions to be performed after each request coming from the client-side. 
@app.after_request
def track_time(response):
    global start_time
    global previous_path

    # Every time the user requests default route (/), time spent in the previous path is recorded in the database with log_data(). 
    if request.path == '/':
        log_data()
        # Update start_time and previous_path
        start_time = datetime.now()
        previous_path = 'HomePage'

    # Every time the user requests /learn_more route, time spent in the previous path is recorded in the database with log_data(). 
    if request.path == '/westsidestory':
        log_data()
        # Update start_time and previous_path
        start_time = datetime.now()
        previous_path = 'Bike Route'

    if request.path == '/tips':
        log_data()
        # Update start_time and previous_path
        start_time = datetime.now()
        previous_path = 'Tips'

    if request.path == '/roadrules':
        log_data()
        # Update start_time and previous_path
        start_time = datetime.now()
        previous_path = 'Road Rules'

    if request.path == '/bikingvspublictransport':
        log_data()
        # Update start_time and previous_path
        start_time = datetime.now()
        previous_path = 'Biking vs Public transport'

    if request.path == '/westsidestory':
        log_data()
        # Update start_time and previous_path
        start_time = datetime.now()
        previous_path = 'Westside Story'

    if request.path == '/rental':
        log_data()
        # Update start_time and previous_path
        start_time = datetime.now()
        previous_path = 'Rental'

    # Every time the user requests  /confirmation route, time spent in the previous path is recorded in the database with log_data(). 
    if request.path == '/confirmation':
        log_data()
        try:
            # Delete start_time and previous_path variables. Time spent on /confirmation route is not recorded. 
            del start_time, previous_path
        except:
            pass
    return response

@app.route("/")
def home():
    # Getting the unique id from the webpage url
    visitor_id = request.args.get('uid') 
    if visitor_id:
        # Add ID to session.
        session["visitor_id"] = visitor_id
    return render_template("home.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/roadrules")
def roadrules():
    return render_template("roadrules.html")

@app.route("/bikingvspublictransport")
def bikingvspublictransport():
    return render_template("bikingvspublictransport.html")


@app.route("/westsidestory")
def westsidestory():
    return render_template("westsidestory.html")

@app.route("/rental")
def rental():
    return render_template("rental.html")

@app.route("/confirmation")
def confirmation():
    return render_template("done.html")

@app.route("/log_binary")
def button_tracking():
    try:
        button_click = Button(
            visitor_id=session.get('visitor_id'),
            button=True)
        db.session.add(button_click)
        db.session.commit()
    except: 
        pass
    return redirect('https://goo.gl/maps/Fg9M7xkX2AKy1vFo7') #what do i put here to return the external link does it have to be a dummy variable


if __name__ == '__main__':
    app.run(port=3000, debug=True)