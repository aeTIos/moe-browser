from flask import Flask
from flask import render_template
import json
import requests
import random

def init(): #initializes array with last 100 image urls
    awwnime = requests.get('https://www.reddit.com/r/awwnime/.json?limit=100', headers = {'User-agent': 'aetios.awwnime.viewer0.0.0.0.1'}).json()
    urls = [y["data"]["url"] for y in awwnime["data"]["children"]]
    print('intitialized')
    return urls


def ran_elem(t):	#returns a random element from t
    random.seed()
    return t[random.randint(0,len(t)-1)]

app = Flask(__name__)
urls = init () #initialize


@app.route('/')

def hello_world():
    return render_template('index.html', imgurl = ran_elem(urls)  )

if __name__ == '__main__':
    app.run()

