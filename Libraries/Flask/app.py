from flask import Flask,render_template
app = Flask(__name__)

# this is the trigger point.
@app.route("/") #used to create route or url. 
def index():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_registration")
def perfomance_registration():
    return "something"


app.run(debug = True)