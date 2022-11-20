from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask, render_template, request
from newsapi import NewsApiClient

serviceUsername = "c5a8a16c-36d3-4d27-b6ac-53d266f233b2"
servicePassword = "aa6c8e51-479a-4f46-8b39-9690581bbf6e"
serviceURL = "https://api.au-syd.assistant.watson.cloud.ibm.com/instances/64f42268-0ca3-4f80-97a5-c4457d695b82"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

app = Flask(__name__)


@app.route("/news")
def news():
    api_key =  "nwKGFI9VJ3sf_BPm8wBqk_THAjLVzyiJ9aWBjR6PQtJ1"
   
    newsapi = NewsApiClient(api_key='API_KEY')

    top_headlines = newsapi.get_top_headlines(sources = "the-verge")
    all_articles = newsapi.get_everything(sources = "the-verge")

    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []  
    url_all = []

    for j in range(len(a_articles)):
        main_all_articles = a_articles[j]  

        news_all.append(main_all_articles['title'])
        desc_all.append(main_all_articles['description'])
        img_all.append(main_all_articles['urlToImage'])
        p_date_all.append(main_all_articles['publishedAt'])
        url_all.append(main_article['url'])
       
        all = zip( news_all,desc_all,img_all,p_date_all,url_all)

    return render_template('db.html',all = all)
@app.route("/search",methods = ['POST', 'GET'])
def searchFunct():
    inputText = request.form['nm']
    api_key =  "nwKGFI9VJ3sf_BPm8wBqk_THAjLVzyiJ9aWBjR6PQtJ1"
   
    newsapi = NewsApiClient(api_key='API_KEY')

    top_headlines = newsapi.get_top_headlines(sources="bbc-news")
    all_articles = newsapi.get_everything(q=inputText)

    t_articles = top_headlines['articles']
    a_articles = all_articles['articles']

    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)

    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []  
    url_all = []

    for j in range(len(a_articles)):
        main_all_articles = a_articles[j]  

        news_all.append(main_all_articles['title'])
        desc_all.append(main_all_articles['description'])
        img_all.append(main_all_articles['urlToImage'])
        p_date_all.append(main_all_articles['publishedAt'])
        url_all.append(main_article['url'])
       
        all = zip( news_all,desc_all,img_all,p_date_all,url_all)

    return render_template('db.html', all = all)

def addNewUser(userName,userEmail,userPassword):
    jsondata = {}
    jsondata["userName"] = str(userName)
    jsondata["userEmail"] = str(userEmail)
    jsondata["userPassword"] = str(userPassword)

    myDataBase = client['database1']
    newDocument = myDataBase.create_document(jsondata)


def authenticate(userName,userEmail):
    myDataBase = client['database1']
    result_collection = Result(myDataBase.all_docs, include_docs=True)
    for data in result_collection:

        if data['doc']['userName'] == str(userName):
            return True
        if data['doc']['userEmail'] == str(userEmail):
            return True
    return False

def authenticateLogin(userEmail,userPassword):
    myDataBase = client['database1']
    result_collection = Result(myDataBase.all_docs, include_docs=True)
   
    for data in result_collection:
        if data['doc']['userPassword'] == str(userPassword) and data['doc']['userEmail'] == str(userEmail):    
            return True
    return False
@app.route("/login",methods = ['POST', 'GET'])
def loginUser():
   
    userEmail = request.form.get("email")
    userPassword = request.form.get("pswd")


    if(authenticateLogin(userEmail,userPassword)):
       return news()
    return render_template("db.html")

@app.route("/registeration",methods = ['POST', 'GET'])
def registerUserData():
    userName = request.form.get("un")
    emailid = request.form.get("ei")
    Phonenumber = request.form.get("pn")
    location = request.form.get("l")
    gender = request.form.get("g")
    Password = request.form.get("p")
    confirmationPassword = request.form.get("cp")
   
    print(userName,emailid,Phonenumber,location,Password,confirmationPassword)
    if(authenticate(userName="username,email id,phone number,location,password,confirmation password")):
        return render_template("signin.html")
    addNewUser(userName,emailid,Phonenumber,location,Password,confirmationPassword)
    return news()

@app.route("/db")
def home():
    return render_template("db.html")

@app.route("/contact")
def hh():
    return render_template("contact.html")
   
@app.route("/aboutus")
def hh():
    return render_template("aboutus.html")
@app.route("/help")
def home():
    return render_template("help.html")

@app.route("/aboutversion")
def home():
    return render_template("aboutversion.html")
