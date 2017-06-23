from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
import oauth2 as oauth

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1238348797-5GmDO5kldGC5tB5A6r0knWePIaR0a3crRBjwwMp'
ACCESS_SECRET = 'Ob28F909WOIda5R45dXcWlVeBkbyCZWKcEaAGy1cFalHV'
CONSUMER_KEY = 'o5p2TNGv19WkEfu324YInDlZT'
CONSUMER_SECRET = 'JnrFeTU0OepvxkUmt2D5ajEm3wY6Mwvficf0lW1tdGQwg5i6eJ'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
my_gen = (item for item in tweets if item[u'text'].find('you') > -1)

@app.route('/')
def home():
    global my_gen
    tweetaronis = []
    for item in my_gen:
        tweet = unicode(item[u'user'][u'screen_name'] + ': ' + item[u'text'] + '\n')
        tweetaronis.append(tweet)
    return render_template('home.html', entries=tweetaronis)
