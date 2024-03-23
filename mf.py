from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost/flask'

db = SQLAlchemy(app)

class Contact(db.Model):
    id = Column(db.Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    msg = Column(String(255), nullable=False)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        msg = request.form.get('msg')
        entry = Contact(username=name, email=email, phone=phone, msg=msg)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')


