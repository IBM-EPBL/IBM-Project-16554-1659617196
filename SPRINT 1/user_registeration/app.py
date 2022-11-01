from urllib import request
from flask import Flask,render_template,request,url_for
from mydb import connect as db
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/result",methods=['POST'])
def send_data():
    name=request.form['exampleInputEmail1']
    print(name)
    #db.insert_values(name,email)
    return "got it"

if __name__=="_main_":
    app.run(debug=True)
