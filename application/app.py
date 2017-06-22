from flask import Flask

app = Flask(__name__)

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1238348797-5GmDO5kldGC5tB5A6r0knWePIaR0a3crRBjwwMp"'
ACCESS_SECRET = 'Ob28F909WOIda5R45dXcWlVeBkbyCZWKcEaAGy1cFalHV'
CONSUMER_KEY = 'o5p2TNGv19WkEfu324YInDlZT'
CONSUMER_SECRET = 'JnrFeTU0OepvxkUmt2D5ajEm3wY6Mwvficf0lW1tdGQwg5i6eJ'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)


@app.route('/')
def home():


    # Get a sample of the public data following through Twitter
    iterator = twitter_stream.statuses.sample()

    # Print each tweet in the stream to the screen
    # Here we set it to stop after getting 1000 tweets.
    # You don't have to set it to stop, but can continue running
    # the Twitter API to collect data for days or even longer.
    tweet_count = 1000
    tweets = {}
    for tweet in iterator:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        tweets += json.dumps(tweet)

        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)

        if tweet_count <= 0:
            break
    return json.dumps(tweets)
