from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

@ app.route("/home")
def home():
    return"This is the home page of the website <h1>JAINIL KADAKIA <h1>" 


"""@app.route("/<id>")
def user(id):
    return f"Hello {id}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/desk")
def desk():
    return redirect(url_for("user",id="36"))"""

@app.route("/")
def Fintech_Solutions():
    return render_template ("main.html",ai=["sam","altman","bill","gates"])

"""@app.route("/<name>")
def Fintech_solutions(name):
    return render_template("main.html",USER=name)"""








