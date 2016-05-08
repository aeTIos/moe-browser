import requests
import json
import random

def init():
	awwnime = requests.get('https://www.reddit.com/r/awwnime/.json?limit=100', headers = {'User-agent': 'aetios.awwnime.viewer0.0.0.0.1'}).json()
	urls = [y["data"]["url"] for y in awwnime["data"]["children"]]
	print('intitialized')
	return urls
def url(urls):	
	random.seed()
	return urls[random.randint(0,len(urls)-1)]

	
