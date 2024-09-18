from flask import Flask, render_template , request
from database import DatabaseHandler


app=Flask(__name__)
app.config["SECRET_KEY"] = "FoulTarnished"
db = DatabaseHandler("appData.db")
db.createTables()


##routing
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/createUser", methods =["post"])
def createUser():
    username=request.form["account name"]
    password=request.form["password"]
    repassword=request.form["re-enter password"]
    if password == repassword:
        db.createUser(username,password)
        return "<h1>SUCCESS</h1>"
    else:
        return "<h1>PASSWORDS DO NOT MATCH</h1>"

##########
app.run(debug = True)