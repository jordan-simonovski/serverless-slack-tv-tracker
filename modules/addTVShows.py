import requests
import slackConnector
import slackMessages
import dynamo
import json

def get_selected_show(payload):
	show_details = {}
	show_details['show_id'] = payload['actions'][0]['value']
	show_details['show_name'] = payload['actions'][0]['name']
	show_details['user_id'] = payload['user']['id']
	show_details['user_name'] = payload['user']['name']
	return show_details

def add_new_tv_show(request_payload):
	request_payload = json.loads(request_payload)
	show_details = get_selected_show(request_payload)
	dynamo.add_show(show_details)
	slackConnector.post_regular_slack(request_payload['response_url'], slackMessages.build_added_show_message(show_details))