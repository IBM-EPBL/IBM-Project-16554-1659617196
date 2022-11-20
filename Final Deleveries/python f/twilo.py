from flask import os
from flask import Flask, render_template,raw_input,bookmark
from twilio.rest import Client
import keys
import subprocess
client = Client(keys.account_sid, keys.auth_token)
def bookmark_func():
    response = raw_input("Please enter the directory name:")
    print("The input directory is",response)
    os.chdir(response)
    cwd = os.getcwd()
    print("Current working directory is:",cwd)
    response2 = raw_input("Please enter a bookmark variable")
    subprocess.call([bookmark, response2])
bookmark_func()
message = client.messages.create(
    body = subprocess.call([bookmark, response2])
   


)
print(subprocess.call([bookmark, response2]))