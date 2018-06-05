import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'CXds2B6qSTGl46EycFLOTNMyG'
CONSUMER_SECRET = 'XhvTN7pr3yWAaxCn8tlxTdVf9VUaFqDB3erfi5jxEupkPYrCf4'
ACCESS_KEY = '997193940959940610-gfTwzyLAxr94Kn6vW70ohPWiouNcxsG'
ACCESS_SECRET = 'CcbmEAMiwnRPIQzpg3wyq9rhJ6FKvcuF27Jsr23P6eM5h'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
   api.update_status(line)
   time.sleep(3600)
# Balfour Bot will tweet every hour with this code