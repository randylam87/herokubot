# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "iTtiiLTVmDYov3ejbYvEJpAn8"
consumer_secret = "JTP9VhK7VWbtY5qqCvzszUPZgRHxZLw2h00eDj4foYrkoMzr0g"
access_token = "56618072-iW8eIJk6Y7qTQkFtm4hHJNFbeXieXV2YNof3G87jx"
access_token_secret = "40Vh5qyFKomBJ45e2DDtIW9XfKYx4yqulcqlFqyA56i3H"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    print('Sending a tweet out then waiting 10 secs')
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #### %s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 10 seconds before doing anything else
    time.sleep(10)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
