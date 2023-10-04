import tweepy
from tweepy import OAuthHandler

def process_or_store(tweet):
    print(json.dumps(tweet))


consumer_key = 'F0N5SEUKJngMz2AT0xUQKxbl0'
consumer_secret = '413SDix7h1EjRvzSrCBWDVQA6kcRAIITh75ulSV0ZiN7Ulp1a6'
access_token = '1709258612210888705-2R7nGhqxzIdY6q723i9qRbBkvvmiSd'
access_secret = 'DsilVsCxiHn93Rt6lh2lqbfSJoJ8XMygtJEqKpr9BGbQ5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api= tweepy.API(auth)

#read my own timeline with limit of 10 tweets
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)

#these do the same thing but with json
for status in tweepy.Cursor(api.friends).items(10):
    process_or_store(status._json)
   
#prints all the followers 
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

# prints all the tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
    