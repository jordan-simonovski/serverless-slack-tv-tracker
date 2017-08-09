from flask import Flask, jsonify, json, request
from zappa.async import task
from modules import *

app = Flask(__name__)

@task
def find_shows(request_form):
	getTVShows.search_tv_shows(request_form['text'], request_form['response_url'])

@app.route('/', methods=['GET','POST'])
def hello_world():
	return "Hello World"

@app.route('/addshow', methods=['GET','POST'])
def find_show():
	find_shows(request.form)
	return('',204)

@app.route('/addshowresponse', methods=['GET','POST'])
def add_new_show():
	addTVShows.add_new_tv_show(request.form['payload'])
	return('',204)

def postDiscussionThread(req, res):
	return getEpisodeUpdates.postPostDiscussionThread()

def getShows(req, res):
	return getEpisodeUpdates.postUpcomingEpisodes()