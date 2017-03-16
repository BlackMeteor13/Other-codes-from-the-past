
import tweepy
import time
import random

# REPLACE these strings with the corresponding information from your Twitter application:
CONSUMER_KEY = 'AxXct4I4QWQwMP4u51gn03yhN'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Y6OQub7Efk6AzHPOq9WXQDnXewS4iI3EqRpZU0RDECokPxnXKp'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '780596002545807360-uOJXxW3xudOrcF8qK3gILoI2Pm6CPXc'#keep the quotes, replace this with your access token
ACCESS_SECRET = '2OOUS6tPEB30ikUFpapF1zWFEavG4hD0UF6E6zB3s00Lw'#keep the quotes, replace this with your access token secret

# Don't touch this :)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Put your code below this line!




poetry = ["Athlete,", "virtuoso,", "Training for happiness," "Bend arm and knee, and seek",
"The body's sharp distress,", "For pain is pleasure's cost,", "Denial is route", "To speech before the millions",
"Or personal with the flute.", "The ape and great Achilles,"]

poetry2 = ["Heavy with their fate,", "Batter doors down, strike",
"Small children at the gate,", "Driven by love to this,", "As knock-kneed Hegel said,",
 "To seek with a sword their peace,", "That the child may be taken away", "From the hurly-burly and fed." ]


#print (poem)
#print (poem2)
#print (poem3)

# My code here will tweet "Tweet tweet" every 15 minutes, 100,000 times. (Will finish in ~3 years).

for i in range(0,10):

    poem = random.choice( poetry )  #pick a random object from list 1
    poem2 = random.choice( poetry2 ) #pick a random object from list 2

    read = poem + " " + poem2 #combinging two lists

    api.update_status(read) #THIS LINE SENDS THE TWEET

    time.sleep(10)#Tweet every hour

