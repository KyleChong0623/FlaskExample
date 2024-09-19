from flask import Flask, render_template , request, redirect
from database import DatabaseHandler
from .route.home import homeBlueprint

app=Flask(__name__)
app.config["SECRET_KEY"] = "FoulTarnished"
db = DatabaseHandler("appData.db")
db.createTables()


##routing
app.register_blueprint(homeBlueprint)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/createUser", methods =["post"])
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

##########
app.run(debug = True)