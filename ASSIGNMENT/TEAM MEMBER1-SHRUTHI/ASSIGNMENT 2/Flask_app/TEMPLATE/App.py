from ast import With
from ftplib import MSG_OOB
from os import uname
from socket import MSG_BCAST, MSG_BTAG
from typing import final
from flask import Flask,render_template,request,redirect
import sqlite3 as sql
import Models as dbHandler

app=Flask(__name__)
app.secret_key='fasdgfdgdfg'


@app.route('/')
def home():
    return
render_template('home.html')


@app.route('/adduser')
def new_user():
    return
render_template('add_user.html')

@app.route('/addrec',methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            email = request.form['email']
            uname = request.form['username']
            rollno = request['rollnumber']
            password = request['password']

            with sql.connect("user_database.db")as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Users (email,username,rollnumber,password  VALUES(?,?,?,?)",(email,uname,rollno,password))
                con.commit()
                msg = "Record Successfully added!"
        except:
            con.rollback()
            msg ="error  in insert operation"

        finally:
            return
    render_template("list.html",msg=msg)
    con.close()   

@app.route('/list')
def list():
    con = sql.connect("User_database.db")
    con.row_factory = sql.Row

    cur=con.cursor()
    cur.execute("select * from users")

    users=cur.fetchall()
    return
render_template("list.html,users = users")


if __name__ == '_main_' :
    app.run(debug = True)

@app.route("/delete")
def delete():
    return
render_template("delete.html")

@app.route('/deleterecord',methods=["POST"])
def deleterecord():
    username = request.form['username']
    with sql.connect("user_database.db")as con:
        try:
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE username = ?",[uname])
            con.commit()
            msg ="Record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return
render_template("home1.html",msg = MSG_BCAST)

if __name__ == '_main_':
    app.run(debug = True)

@app.route('/deldb', methods = ["POST"])
def deldb():
    con = sql.connect('User_database.db')
    cur = con.cursor()
    cur.execute('DELETE FROM users;')
    con.commit()
    con.close()
    msg ='All the data has been deleted'
    return
render_template("home1.html",msg = MSG_BTAG)


@app.route("/log")
def log():
    return render_template("login.html")


@app.route('/login', methods =['GET','POST'])
def login():
    username = request.form['username']
    if request.method=='POST':
        users=dbHandler.retrieveUsers()
        msg = 'Logged in successfully!'
        return render_template('welcome.html',users=uname,msg=msg)

    else:
        msg='You are not registered,would you like to be registered'
        return render_template('home1.html',msg=msg)

if __name__ == '_main_':
    app.run(debug = False,host='0.0.0.0')


                