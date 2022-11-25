from flask import Flask, render_template, request, redirect, url_for,session

import ibm_db
import bcrypt
try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=saru.crt;PROTOCOL=TCPIP;UID=ctj72194;PWD=EVf6WD5LAM5ViY2k",'','')
    print(conn)
    print("connection successfull")
except:
    print("Error in connection, sqlstate = ")
    errorState = ibm_db.conn_error()
    print(errorState)
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET'])
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', name='Home')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']

        if not email or not name or not password or not cpassword:
            return render_template('register.html', error='Please fill all fields')
        if password != cpassword:
            return render_template('register.html', error='The password is not same')
        else:
            hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            print(type(hash))
            print(hash)
            #encpass=hash.decode()
            #print(encpass)
            #print(type(encpass))


        query = "SELECT * FROM userlogin WHERE useremail=?"
        stmt = ibm_db.prepare(conn, query)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        isUser = ibm_db.fetch_assoc(stmt)

        if not isUser:
            insert_sql = "INSERT INTO userlogin(USERNAME, USEREMAIL, PASSWORD) VALUES (?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, hash)
            ibm_db.execute(prep_stmt)
            return render_template('login.html', success="You can login")
        else:
            return render_template('register.html', error='Invalid Credentials')

    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            return render_template('login.html', error='PLEASE FILL ALL FIELDS')
        query = "SELECT * FROM userlogin WHERE useremail=?"
        stmt = ibm_db.prepare(conn, query)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        isUser = ibm_db.fetch_assoc(stmt)
        print(isUser, password)

        if not isUser:
            return render_template('login.html', error='INVALID USERNAME OR PASSWORD')
        # return render_template('login.html',error=isUser['PASSWORD'])

        isPasswordMatch = False
        temp=str(isUser['PASSWORD'])
        temp=temp.replace("\x00",'')
        temp=temp[2:len(temp)-1]
        print(temp)
        temp = temp.encode("utf-8")
        print(temp,type(temp))
        check = bcrypt.hashpw(password.encode('utf-8'),temp)
        #print(check==temp[:len(check)])
        if check==temp[:len(check)]:
            isPasswordMatch=True
        #isPasswordMatch = bcrypt.checkpw(password.encode('utf-8'), isUser['PASSWORD'])

        if not isPasswordMatch:
            return render_template('login.html', error='Invalid Credentials')

        session['email'] = isUser['USEREMAIL']
        return redirect(url_for('dashboard'))

    return render_template('login.html', name='Home')


@app.route('/logout.html')
def logout():
    return render_template("login.html")
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
@app.route('/about.html')
def about():
    return render_template("about.html")
@app.route('/Contact.html')
def Contact():
    return render_template("Contact.html")
@app.route('/help.html')
def help():
    return render_template("help.html")
@app.route('/news.html')
def news():
    return render_template("news.html")
@app.route('/bundle.js')
def bundle():
        return render_template("bundle.js")

if __name__ == "__main__":
    app.run(debug=True)

    #$2b$12$jEdIBY4xNTU0TIR96mpU/e1tFv2k1x42.TBfRhgO7utWp1VU8olZ
    #$2b$12$jEdIBY4xNTU0TIR96mpU/eRtrmKE.BtEgYCuVoBGWRqu8.4T0dAPC

    #$2b$12$1Nr6EFqqgPAPXg5eeFe3M.2s8Kt.weE78eMk8ZxTBaUf2gmY2ykLq