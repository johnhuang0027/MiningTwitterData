import tweepy
from tweepy import OAuthHandler

consumer_key = 'F0N5SEUKJngMz2AT0xUQKxbl0'
consumer_secret = '413SDix7h1EjRvzSrCBWDVQA6kcRAIITh75ulSV0ZiN7Ulp1a6'
access_token = '1709258612210888705-2R7nGhqxzIdY6q723i9qRbBkvvmiSd'
access_secret = 'DsilVsCxiHn93Rt6lh2lqbfSJoJ8XMygtJEqKpr9BGbQ5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
