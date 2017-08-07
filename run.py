from flask import Flask, jsonify, json
from flask import request
from modules import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
	return "Hello World"

def postDiscussionThread(req, res):
	return tvdbconnect.postPostDiscussionThread()

def getShows(req, res):
	return tvdbconnect.postUpcomingEpisodes()