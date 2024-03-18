from flask import Flask,render_template,request,redirect,url_for,session,flash
from datetime import timedelta




app = Flask(__name__)




@app.route("/")
def home():
    
    return"new deploymnet"




app.secret_key = "JAINIL" 
app.permanent_session_lifetime= timedelta(minutes=5)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent =True
        user = request.form["username"]
        session["user"] = user
        
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>Welcome, {user}</h1>"
    else:
        return redirect(url_for("login"))

app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

    

if __name__ == "__main__":
    app.run()
