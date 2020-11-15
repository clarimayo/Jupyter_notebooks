import requests
from bs4 import BeautifulSoup
from flask import Flask 

URL = 'https://worldpoverty.io/headline'
page = requests.get(URL)

soup = BeautifulSoup(page.content)
  #browser host

app = Flask('webapp')
@app.route('/')
def home():
    return soup