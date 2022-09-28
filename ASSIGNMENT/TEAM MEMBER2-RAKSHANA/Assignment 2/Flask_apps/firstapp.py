from collections import UserDict
from flask import Flask, render_template, request,redirect, url_for, session,ibm_db
import re

app = Flask(__name__)

app.secretary_key = '7894'

conn = ibm_db.connect("DATABASE=;HOSTNAME=;PORT=;SECURITY=SSL;SSLServerCertificate=;UID=;PWD=",'','')

@app.route('/')
def home():
    return render_template('register.html')


@app.route('/login',methods =['GET','POST'])
def login():
    global Userid
    msg = ''

    if request.method== 'POST':
        username = request.form['username']
        password = request.form['password']


        sql = "SELECT * FROM Users WHERE username =? AND password=?"
        stmt = ibm_db.prepare(conn,sql)

        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account =ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['Loggedin']=True
            session['id']=account['username']
            userid = account['USERNAME']
            session['username']= account['USERNAME']
            msg = 'Logged in successfully'
            return render_template('welcome.html', msg=msg, username=username)
        else:
            msg="Incorrect username/password"
            return render_template('login.html',msg=msg)


@app.route('/register', methods=[ 'GET','POST'])
def register():
    if request.method == 'POST':
        username =request.form['username']
        email = request.form['email']
        password =request.form['password']
        sql ="SELECT * FROM users WHERE username=?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg ="Account already exists"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            msg = "Invalid email address"
        elif not re.match(r'[A-Za-z0-9]+',username):
            msg ="name must contain characters and numbers"
        else:
            insert_sql ="INSERT INTO users VALUES(?,?,?)"
            prep_stmt = ibm_db.prepare(conn.insert_sql)
            ibm_db.bind_param(prep_stmt,1,username)
            ibm_db.bind_param(prep_stmt,2,email)
            ibm_db.bind_param(prep_stmt,3,password)
            ibm_db.execute(prep_stmt)
            msg ="You have successfully registered"

        return render_template('register.html',msg=msg)



@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
