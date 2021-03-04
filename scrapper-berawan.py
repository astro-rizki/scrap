import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tweepy import OAuthHandler, Stream, StreamListener
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="zj6hOR9GXVJYt2lr2FZKU1Q1G"
consumer_secret="0bXsZryRQixl5rvHSbfJYQnvGJirsCH0K6CV1XNz7efBT4fUgo"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1184880065546313728-TZIL5FB0fvMwTAWEEjyUY7TaO2tVVl"
access_token_secret="F7KiOSvS1qMGFoG0wMvcQ6IFoB310eG9qxGkwNomWSiqb"

# Use a service account
cred = credentials.Certificate('login.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        # print(data)
        json_data = json.loads(data)
        doc_name= json_data["id_str"]
        doc_ref = db.collection(u'tweet-berawan').document(u''+doc_name)
        doc_ref.set(json_data)
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True

# doc_ref = db.collection(u'users').document(u'alovelace2')
# doc_ref.set({
#     u'first': u'Ada2',
#     u'last': u'Lovelace',
#     u'born': 1815
# })


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['berawan'])