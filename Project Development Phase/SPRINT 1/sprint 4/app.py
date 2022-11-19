from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask, render_template, request 
from newsapi import NewsApiClient
from pushbullet import PushBullet
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import time
access_token =  "7318f37439ea9a3d1fb65fd1846ac9b0"
data = input(newsapi = NewsApiClient(api_key='API_KEY'))
text = textarea("Text", rows=3, placeholder="Write some text...",
required=True)
pb = PushBullet (access_token)
push = pb.push_note (data, text)
put_success("Message sent successfully...") 
time.sleep(3)
clear()
toast("Thanks for Using :)")
hold()

def news():
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
