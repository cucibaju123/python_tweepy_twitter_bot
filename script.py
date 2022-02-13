import tweepy
import os
import random
import schedule
import time
from dotenv import load_dotenv


class TwitterSecrets:
    """Class that holds Twitter Secrets"""

    def __init__(self):
        # load keys from .env file, so we can use os.environ.get()
        load_dotenv()
        self.TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
        self.TWITTER_API_SECRET = os.environ.get("TWITTER_API_SECRET")
        self.TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
        self.TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")
        self.TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")

        # Tests if keys are present
        for key, secret in self.__dict__.items():
            assert secret != "", f"Please provide a valid secret for: {key}"


def tweet():
    secrets = TwitterSecrets()
    # authenticatng to use Twitter API key
    auth = tweepy.OAuthHandler(secrets.TWITTER_API_KEY, secrets.TWITTER_API_SECRET)
    # Set access token and secret so all API requests will be on our account's behalf
    auth.set_access_token(secrets.TWITTER_ACCESS_TOKEN, secrets.TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    list_of_tweets = []

    with open("gentext.txt", "r") as file:
        for row in file.readlines():
            list_of_tweets.append(row)

    # Generate text tweet
    api.update_status(random.choice(list_of_tweets))


# Schedule a tweet at 19:00 everyday
schedule.every().day.at("19:00").do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
