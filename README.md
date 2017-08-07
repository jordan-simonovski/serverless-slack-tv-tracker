# slack-tvbot
A Bot for tracking TV shows, and creating discussion threads in public slack channels

## Setup

### Getting Started
```bash
cd slack-tvbot
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### How to even zappa_settings.json 

```json

{
    "dev": {
        "app_function": "run.app", 
        "aws_region": "ap-southeast-2", 
        "profile_name": "personal", 
        "s3_bucket": "zappa-slacktvbot-2017-jfksdjfksjkds",
        "environment_variables": {
            "tvdbAPIKey": "insert key here",
            "tvdbUserKey": "insert user key here",
            "tvdbUserName": "obama",
            "slackWebhook": "webhookurl",
            "timezone": "Australia/Sydney"
        },
        "events": [
            {
               "function": "run.postDiscussionThread", 
               "expression": "cron(0 9 * * ? *)" 
            },
            {
                "function": "run.getShows", 
                "expression": "cron(0 12 * * ? *)"
            }
        ]
    }
}

```

1. You will need to set up a TVDB account and get your API and user keys.
2. You will also need to set up your slack webhook in order for the bot to be able to post to a particular channel
3. The crons set up determine when a post will be made (cron in UTC)


### Hosting the bot

```bash
// This sets up your dev version of the app.
zappa deploy dev
```

### Invoking Commands manually

```bash
// This will find all of the shows airing today and 
// post them to slack

zappa invoke dev run.getShows


// This will find shows that were set to air today
// and start a post-episode discussion thread on slack

zappa invoke dev run.postDiscussionThread

```

## Current Features

- tracking a list of hardcoded series using TVDB
- notifications of upcoming episodes of a series 
- post-episode discussion threads

## Planned Features

- slash command to add tv shows to track
- tracking and posting to more than one channel
- List of legal ways to watch episode (planning to integreate with https://pypi.python.org/pypi/JustWatch/0.4.1)