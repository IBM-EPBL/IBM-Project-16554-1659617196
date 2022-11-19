from flask import os
from flask import Flask, render_template,raw_input,bookmark
import requests
import subprocess
def bookmark_func():
    response = raw_input("Please enter the directory name:")
    print("The input directory is",response)
    os.chdir(response)
    cwd = os.getcwd()
    print("Current working directory is:",cwd)
    response2 = raw_input("Please enter a bookmark variable")
    subprocess.call([bookmark, response2])
bookmark_func()
resp = requests.post('https://textbelt.com/text', {
  'phone': '5555555555',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())