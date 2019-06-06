import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

ACCESS_TOKEN = '33093650-lMlbx8bcuRLVkj5pMEiq8DBJowq2k3M8gDm7JdHKX'
ACCESS_TOKEN_SECRET = 'ZsFfmHcZBMVSmS1r8lB5F1YVhbIKRNRmWiwECN8ars'
CONSUMER_KEY = '5sk7dKsZGWfSycMZhRN8F93SW'
CONSUMER_SECRET = 'CIKf9lN29zhnw6U6dc0GWtiWaaBYSwmBrcgHpUtCdqabRoAqql'

class TwitterStreamer():
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #This handles Twitter authentication and the connection to the Twitter Streaming API.
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        
        stream = Stream(auth, listener)
        
        stream.filter(track = hash_tag_list)

class StdOutListener(StreamListener):
    
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    
    hash_tag_list = ['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders']
    fetched_tweets_filename = 'tweets.json'
    
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)


