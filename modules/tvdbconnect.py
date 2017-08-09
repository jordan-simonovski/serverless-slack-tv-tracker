import requests
import os

apiKey = os.environ.get("tvdbAPIKey")
userKey = os.environ.get("tvdbUserKey")
username = os.environ.get("tvdbUserName")

baseUrl = "https://api.thetvdb.com"
headers = { "Content-Type": "application/json", "Accept": "application/json" }

def connect():
    loginUrl=baseUrl+"/login"
    payload = '{ "apikey": "'+apiKey+'", "username": "'+username+'", "userkey": "'+userKey+'" }'
    response = requests.post(url=loginUrl, data=payload, headers=headers)
    data = response.json()
    headers['Authorization'] = "Bearer " + data['token']
    return headers