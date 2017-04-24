#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "403483808-NmJwlXtHkfRFfdIpNsa0mKFGDRPkAQh9gfH0OHWW"
access_token_secret = "bwGRpen6SdmCIFqeFcnTPyPg5IomP8NtzwhmU8tWVMrgj"
consumer_key = "xdt4REI2mu33QgrLgTLQRlsge"
consumer_secret = "5GwTwQ898MpihZDPuUZme0JkWeuHS0YwEgtipxoYfBbvwy6F95"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        f = open('twitJoziSA.txt', 'a')
        f.write(data)
        f.close()
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Johannesburg', 'South Africa', 'Jozi', 'Joburg'])