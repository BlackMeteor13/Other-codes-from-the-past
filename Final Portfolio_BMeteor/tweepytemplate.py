#import tweepy
import time

# REPLACE these strings with the corresponding information from your Twitter application:
CONSUMER_KEY = 'umDzbXrqoqGR0BlkonIjnnOUM'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'oFn2yCEkQcBaMwr4HRDTkC9MxOuGAZvoZWbMFE4NahSeZtLmiR'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '509699299-94m35y0tTb5yP3HcKk5DAQyYdzGdu4d3Dfb0R3L0'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'BhdTxWtSLCiJa0MsAO8qOEsx9DvYl4JiZI3EnXuQDvNJl'#keep the quotes, replace this with your access token secret

# Don't touch this :)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Put your code below this line!

import random
 

poetry = ["Athlete,", "virtuoso,", "Training for happiness," "Bend arm and knee, and seek", 
"The body's sharp distress,", "For pain is pleasure's cost,", "Denial is route", "To speech before the millions", 
"Or personal with the flute.", "The ape and great Achilles,", "Heavy with their fate,", "Batter doors down, strike", 
"Small children at the gate,", "Driven by love to this,", "As knock-kneed Hegel said,",
 "To seek with a sword their peace,", "That the child may be taken away", "From the hurly-burly and fed." ]

poem = random.choice( poetry )
poem2 = random.choice( poetry )
poem3 = random.choice( poetry )

print (poem)
print (poem2)
print (poem3)

# My code here will tweet "Tweet tweet" every 15 minutes, 100,000 times. (Will finish in ~3 years).

for i in range(0,100000):
	api.update_status(poem+poem2+poem3) # THIS LINE SENDS THE TWEET: "Tweet tweet"
	time.sleep(900) #Tweet every 15 minutes
