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