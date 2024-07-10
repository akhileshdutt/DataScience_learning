from flask import Flask,render_template,request
from database import databases
app = Flask(__name__)

databases_object = databases()
# this is the trigger point.
@app.route("/") #used to create route or url. 
def index():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/perform_registration", methods=['POST'])
def perfomance_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = databases_object.insert_data(name,email,password)
    if(response==1):
        return "Registration Successful"
    else:
        return "User Already Registered"
     


app.run(debug = True)