import requests
import os
import slackMessages
import json

slackWebhook = os.environ.get("slackWebhook")

def post_regular_slack(webhook, message):
	requests.post(webhook, data=message)

def post_to_channel(message):
	requests.post(slackWebhook, data=message)

def isMultipleEpisodes(recentEpisodeJson):
	return len(recentEpisodeJson['episodeList']) > 1

def postUpcomingShows(episodeJson):
	for showName, showEpisode in episodeJson.items():
		if (isMultipleEpisodes(showEpisode['recentEpisode'])):
			episodeList = ",".join(str(x) for x in showEpisode['recentEpisode']['episodeList'])
			showJson = slackMessages.buildMultipleEpisodeJson(showName, showEpisode, episodeList)
			requests.post(slackWebhook, data=json.dumps(showJson))
		elif 'episodeName' in showEpisode['recentEpisode']:
			showJson = slackMessages.buildUpcomingSlackJson(showName, showEpisode)
			requests.post(slackWebhook, data=json.dumps(showJson))

def postPostDiscussionThread(episodeJson):
	for showName, showEpisode in episodeJson.items():
		if 'episodeName' in showEpisode['recentEpisode']:
			showJson = slackMessages.buildPostDiscussionThread(showName, showEpisode)
			requests.post(slackWebhook, data=json.dumps(showJson))