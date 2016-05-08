from flask import Flask
from flask import render_template
import json
import requests
import jsonstuff


app = Flask(__name__)
urls = jsonstuff.init()
print('test')

@app.route('/')

def hello_world():
    return render_template('index.html', imgurl=jsonstuff.url(urls)  )

if __name__ == '__main__':
    app.run()


