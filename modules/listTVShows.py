import slackConnector
import slackMessages
import dynamo
import json

def get_show_items():
	return dynamo.list_shows()

def get_shows():
	shows = get_show_items()
	slackConnector.post_to_channel(slackMessages.build_show_list_message(shows))