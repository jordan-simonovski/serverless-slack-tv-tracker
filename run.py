from flask import Flask, jsonify, json
from flask import request
from modules import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
	return "Hello World"

@app.route('/addshow', methods=['GET','POST'])
def add_show():
	getTVShows.search_tv_shows(request.form['text'], request.form['response_url'])
	return('',204)

def postDiscussionThread(req, res):
	return getEpisodeUpdates.postPostDiscussionThread()

def getShows(req, res):
	return getEpisodeUpdates.postUpcomingEpisodes()