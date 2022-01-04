import tweepy
import time

auth = tweepy.OAuthHandler('5tyKYEBU0ROhX1zafLiQdyqs5', 'tOn06abGpYcfQir9ttpm9V9vU0MWmnOOEP9Ek5PQsjWqNtewTB')
auth.set_access_token('1330981662667264003-UsOJ1PWTMSE5zmY5sKVYXN4HMgExa4', 'BCynI8MTG9g0ZvtipYP8MsyEXK2oGtLgsrDa9PPJCTHlh')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
    except StopIteration:
        return

serch_string = 'Python'
numbersOfTweets = 2

#hacer que el boot busque determinada palabra en un tweet y si esta que le de like
for tweet in tweepy.Cursor(api.search, serch_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        #tweet.retweet()  para retuitear los que tienen ese nombre
        print('i like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


#Generous Bot, always folow you back
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'bautiallende':
#         follower.follow()
#         break
