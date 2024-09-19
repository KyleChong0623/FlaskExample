from flask import Blueprint, redirect, render_template, request
from database import DatabaseHandler

signupBlueprint=Blueprint("signup",__name__)
createUserBlueprint=Blueprint("createuser,__name__")
authenticateUserBlueprint=Blueprint("authenticateUser",__name__)

@authenticateUserBlueprint.route("/authenticate",method=["post"])
def authenticateUser():
    db=DatabaseHandler("appData.db")
    username=request.form["username"]
    password=request.form["password"]

@signupBlueprint.route("/signup")
def home():
    return render_template("index.html")

@createUserBlueprint.route("/signup")
def signup():
    return render_template("signup.html")

@createUserBlueprint.route("/createUser", methods =["post"])
def createUser():
    username=request.form["account name"]
    password=request.form["password"]
    repassword=request.form["re-enter password"]
    if password == repassword:
        response=db.createUser(username,password)
        if response==False:
            return redirect("/")
        else:
            return "<h1>Error making account</h1>"
    else:
        return "<h1>PASSWORDS DO NOT MATCH</h1>"
