import tweepy
import os


class TwitterSecrets:
    """Class that holds Twitter Secrets"""

    def __init__(self):
        self.API_KEY = os.environ.get("TWITTER_API_KEY")
        self.API_SECRET = os.environ.get("TWITTER_API_SECRET")
        self.ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
        self.ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")
        self.BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")

        # Tests if keys are present
        for key, secret in self.__dict__.items():
            assert secret != "", f"Please provide a valid secret for: {key}"


secrets = TwitterSecrets()

# authenticatng to use Twitter API key
auth = tweepy.OAuthHandler(secrets.API_KEY, secrets.API_SECRET)
# Set access token and secret so all API requests will be on our account's behalf
auth.set_access_token(secrets.ACCESS_TOKEN, secrets.ACCESS_SECRET)
api = tweepy.API(auth)

# Generate text tweet
api.update_status("This is a test tweet")
