import tvdbconnect
import requests
import slackConnector
import slackMessages

baseUrl="https://api.thetvdb.com"
headers = ""

def search_tv_shows(show_name, response_url):
	headers = tvdbconnect.connect()
	searchTvUrl = baseUrl + "/search/series"
	payload = {"name": show_name}
	response = requests.get(url=searchTvUrl, params=payload, headers=headers)
	data = response.json()
	slackConnector.post_regular_slack(response_url, get_tv_show_message(data))
	get_tv_show_message(data)

def get_tv_show_message(data):
	shows = []
	for show in data['data']:
		show_data = {}
		show_data['seriesName'] = show['seriesName']
		show_data['overview'] = show['overview']
		show_data['id'] = show['id']
		show_data['banner'] = 'http://thetvdb.com/banners/'+show['banner']
		shows.append(show_data)
	message = slackMessages.build_found_shows_message(shows)
	return message