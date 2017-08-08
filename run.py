from flask import Flask, jsonify, json, request
from zappa.async import task
from modules import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
	return "Hello World"

@task
def find_shows(request_form):
	getTVShows.search_tv_shows(request_form['text'], request_form['response_url'])

@app.route('/addshow', methods=['GET','POST'])
def add_show():
	find_shows(request.form)
	return('',204)

def postDiscussionThread(req, res):
	return getEpisodeUpdates.postPostDiscussionThread()

def getShows(req, res):
	return getEpisodeUpdates.postUpcomingEpisodes()