import json
red = "#ff0000"
blue = "#3AA3E3"
spoilerThumb = "http://i.imgur.com/3s0QcvY.jpg"

def buildUpcomingSlackJson(showName, showEpisode):
	slackMessage = {
		"response_type": "in_channel",
		"attachments": [{
			"title": showName,
			"fields": [
				{
					"title": "Air Time",
					"value": showEpisode['recentEpisode']['airTime'],
					"short": "false"
				},
				{
					"title": "Episode Name",
					"value": showEpisode['recentEpisode']['episodeName'],
					"short": "false"
				},
				{
					"title": "Episode Number",
					"value": showEpisode['recentEpisode']['episodeNumber'],
					"short": "false"
				},
				{
					"title": "Rating",
					"value": showEpisode['rating'],
					"short": "false"
				}
			],
			"color": blue,
			"attachment_type": "default",
			"image_url": showEpisode['banner']
		}]
	}
	return slackMessage

def buildMultipleEpisodeJson(showName, showEpisode, episodeList):
	slackMessage = {
		"response_type": "in_channel",
		"attachments": [{
			"title": showName,
			"fields": [
				{
					"title": "Air Time",
					"value": showEpisode['recentEpisode']['airTime'],
					"short": "false"
				},
				{
					"title": "Multiple Episodes have Aired",
					"value": "",
					"short": "false"
				},
				{
					"title": "Episodes",
					"value": episodeList,
					"short": "false"
				},
				{
					"title": "Rating",
					"value": showEpisode['rating'],
					"short": "false"
				}
			],
			"color": blue,
			"attachment_type": "default",
			"image_url": showEpisode['banner']
		}]
	}
	return slackMessage

def buildPostDiscussionThread(showName, showEpisode):
	slackMessage = {
		"response_type": "in_channel",
		"attachments": [{
			"title": showName + ": Post Episode Discussion Thread",
			"pretext": "Please keep this channel spoiler free and post in the thread of this message!",
			"fields": [
				{
					"title": "Episode Name",
					"value": showEpisode['recentEpisode']['episodeName'],
					"short": "false"
				},
				{
					"title": "Episode Number",
					"value": showEpisode['recentEpisode']['episodeNumber'],
					"short": "false"
				},
				{
					"title": "Rating",
					"value": showEpisode['rating'],
					"short": "false"
				}
			],
			"color": red,
			"attachment_type": "default",
			"thumb_url": spoilerThumb
		}]
	}
	return slackMessage

def get_show_list_attachment(show_object):
	user = "<@{0}|{1}>".format(show_object['userID'], show_object['userName'])
	attachment = {
		"callback_id": "list_shows",
		"fields":[{
			"title": show_object['showTitle'],
			"value": "Added by {0}".format(user),
			"short": "false"
		}]
	}
	return attachment

def build_show_list_message(show_list):
	message_attachments = []
	for show in show_list:
		message_attachments.append(get_show_list_attachment(show))
	slack_message = {
		"response_type": "in_channel",
		"title": "TV Shows being tracked:",
		"attachments": message_attachments
	}
	return json.dumps(slack_message)

def get_attachment(show):
	attachment = {
		"callback_id": "add_show",
		"fields":[{"title": show['seriesName'],"value": show['overview']}],"image_url": show['banner'],
		"actions": [{
			"name": show['seriesName'],
			"text": "Add Show",
			"type": "button",
			"value": show['id']}]
		}
	return attachment

def build_found_shows_message(shows):
	message_attachments = []
	for show in shows:
		message_attachments.append(get_attachment(show))
	slack_message = {
		"response_type": "ephemeral",
		"attachments": message_attachments
	}
	return json.dumps(slack_message)

def build_blocked_user_message(show_object):
	user = "<@{0}|{1}>".format(show_object['user_id'], show_object['user_name'])
	slack_message = {
		"response_type": "in_channel",
		"title": "Blocked user found",
		"text": "{0} tried to add the show *{1}*. {0} isn't allowed to. Poor {0}. :troll:".format(user, show_object['show_name'])
	}
	return json.dumps(slack_message)

def build_added_show_message(show_object):
	user = "<@{0}|{1}>".format(show_object['user_id'], show_object['user_name'])
	slack_message = {
		"response_type": "in_channel",
		"title": "New Show Added!",
		"text": "{0} just added the show *{1}* to the tracker.".format(user, show_object['show_name'])
	}
	return json.dumps(slack_message)

