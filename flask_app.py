from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="bozzisql2",
    password="BirilloBlu33",
    hostname="bozzisql2.mysql.pythonanywhere-services.com",
    databasename="bozzisql2$sensors",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Sensor(db.Model):

    __tablename__ = "sensors"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)

comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index'))

