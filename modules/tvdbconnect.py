import requests
import slackConnector
from datetime import *
import os
import pytz


apiKey= os.environ.get("tvdbAPIKey")
userKey= os.environ.get("tvdbUserKey")
username= os.environ.get("tvdbUserName")
tz = pytz.timezone(os.environ.get("timezone"))

baseUrl="https://api.thetvdb.com"
headers = { "Content-Type": "application/json", "Accept": "application/json" }

# Yes, I'm hardcoding IDs for now. Will move these to Dynamo later.
# TV Show IDs hardcoded in respective order: Fargo, American Gods, Silicon Valley, Samurai Jack, Better Call Saul, Brooklyn Nine-Nine
# Archer, Game of Thrones, My Hero Academia, Attack on Titan
seriesIds = ['269613', '253573', '277165', '75164', '273181', '269586', '110381', '305074', '267440', '260315']
# seriesIds = ['269586']

def getTVShowInfo(showName):
    searchTvUrl = baseUrl + "/search/series"
    payload = {"name": showName}
    response = requests.get(url=searchTvUrl, params=payload, headers=headers)
    data = response.json()
    print(data)

def getDate(dateString):
    if not dateString:
        return "" 
    else:
        now = date(*map(int, dateString.split('-')))
        return now

def findRecentEpisode(episodeList):
    episodeInfo = {}
    episodeListObj = []
    for episode in episodeList:
        epDate = getDate(episode['firstAired'])
        if epDate != "":
            americanAdjustment = timedelta(days = 1)
            today = date.today()
            if epDate == today-americanAdjustment:
                episodeNumber = episode['airedEpisodeNumber']
                episodeListObj.append(str(episodeNumber))
                episodeInfo['episodeName'] = episode['episodeName']
                episodeInfo['episodeNumber'] = episodeNumber
                episodeInfo['overview'] = episode['overview']
    episodeInfo['episodeList'] = episodeListObj
    return episodeInfo

def getShowNameAndDescription(showId):
    getShowInfoUrl = baseUrl+"/series/"+showId
    r = requests.get(url=getShowInfoUrl, headers=headers)
    d = r.json()
    return d['data']

def getLocalAirTime(airTime):
    m2 = datetime.strptime(airTime, '%I:%M %p')
    americanAdjustment = timedelta(hours = 14)
    localTime = m2+americanAdjustment
    localisedAirTime = localTime.strftime("%I:%M %p")
    return localisedAirTime

def getEpHasAired(localisedAirTime):
    today = datetime.now(pytz.utc)
    localisedToday = today.astimezone(tz)
    todayTime = localisedToday.strftime("%I:%M %p")
    return todayTime > localisedAirTime

def getEpInfo(showInfo, showId):
    episodeJson = {}
    getEpsUrl = baseUrl + "/series/"+showId+"/episodes"
    r = requests.get(url=getEpsUrl, headers=headers)
    d = r.json()
    showName = showInfo['seriesName']
    episodeJson[showName] = {}
    episodeJson[showName]['recentEpisode'] = findRecentEpisode(d['data'])
    episodeJson[showName]['banner'] = 'http://thetvdb.com/banners/'+showInfo['banner']
    episodeJson[showName]['rating'] = showInfo['rating']
    episodeJson[showName]['recentEpisode']['airTime'] = getLocalAirTime(showInfo['airsTime'])
    return episodeJson

def postPostDiscussionThread():
    tvdbConnect()
    for show in seriesIds:
        showInfo = getShowNameAndDescription(show)
        episodeInfo = getEpInfo(showInfo, show)
        showName = showInfo['seriesName']
        airTime = episodeInfo[showName]['recentEpisode']['airTime']
        if (getEpHasAired(getLocalAirTime(airTime))):
            slackConnector.postPostDiscussionThread(episodeInfo)
    return "ok"

def postUpcomingEpisodes():
    tvdbConnect()
    for show in seriesIds:
        showInfo = getShowNameAndDescription(show)
        episodeInfo = getEpInfo(showInfo, show)
        slackConnector.postUpcomingShows(episodeInfo)
    return "ok"

def tvdbConnect():
    loginUrl=baseUrl+"/login"
    payload = '{ "apikey": "'+apiKey+'", "username": "'+username+'", "userkey": "'+userKey+'" }'
    response = requests.post(url=loginUrl, data=payload, headers=headers)
    data = response.json()
    headers['Authorization'] = "Bearer " + data['token']
