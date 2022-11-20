from urllib import request
from flask import Flask,render_template,request,url_for
from ibm_db import connect
app = Flask(__name__,template_folder='template')


@app.route("/Registeration")
def render_registeration(accountok=True):
    if accountok==True:
         return render_template("index.html",message="")
    else:
        return render_template("index.html",message="username/email id/phone number/location/password/confirmation password")
    

@app.route("/result",methods=['POST'])
def send_data():
    name=request.form['exampleInputEmail1']
    print(name)
    #db.insert_values(name,email id,phone number,gender,location,password,confirmation password)
    return "got it"

if __name__=="_main_":
    app.run(debug=True)