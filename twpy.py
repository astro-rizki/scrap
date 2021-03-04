# import tweepy
# api = tweepy.API(auth)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

from tweepy import OAuthHandler, Stream, StreamListener

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="zj6hOR9GXVJYt2lr2FZKU1Q1G"
consumer_secret="0bXsZryRQixl5rvHSbfJYQnvGJirsCH0K6CV1XNz7efBT4fUgo"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1184880065546313728-TZIL5FB0fvMwTAWEEjyUY7TaO2tVVl"
access_token_secret="F7KiOSvS1qMGFoG0wMvcQ6IFoB310eG9qxGkwNomWSiqb"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data.text)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['hujan'])