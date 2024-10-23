from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres123@localhost/price_collector" # connecting to the database
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(120), unique=True)
    price = db.Column(db.Integer)

    def __init__(self, email, price):
        self.email = email
        self.price = price



@app.route("/", methods=["GET", "POST"])  # decorator with arguments
def index():
    return render_template("index.html") # rendering a template

@app.route("/success", methods=["POST"])  # u must to put the method in the route
def success():
    if request.method == "POST":
        email = request.form["email_name"] # getting the data from the form if the method is POST and the name of the input is email_name
        price = request.form["price_number"]
       
        #print(request.form)
        #print(email, price)
    if db.session.query(Data).filter(Data.email == email).count() == 0:
        db.session.add(Data(email, price)) # adding the data to the database
        db.session.commit()
        average_price = db.session.query(func.avg(Data.price)).scalar()  # scalar() is used to get the average height from the database
        average_price= round(average_price, 1) # rounding the average height
        count = db.session.query(Data.price).count()
        send_email(email, price, average_price, count)
        #print(average_price) 
        db.session.close()
        return render_template("success.html")
    return render_template("index.html", text="Parece que ya tenemos algo de esa dirección de correo electrónico, prueba con otro.")



if __name__ == "__main__": 
    app.run(debug=True)

