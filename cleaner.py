#!/usr/bin/env python

import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''


def oath_login(consumer_key, consumer_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()

    verify_code = raw_input("Authenticate URL: {} - Enter verification code: ".format(auth_url))
    auth.get_access_token(verify_code)

    return tweepy.API(auth)


def delete_tweets(api):
    for status in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(status.id)
        print("Deleted Tweet: {}".format(status.id))


if __name__ == "__main__":
    api = oath_login(CONSUMER_KEY, CONSUMER_SECRET)
    delete_tweets(api)
