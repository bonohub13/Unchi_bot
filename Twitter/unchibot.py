#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy
from time import ctime

class Unchibot:
    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        self.set_msg()
        self.makeAPI().update_status(self.output_msg[0])
        self.init_time = self.current_time

    def set_msg(self):
        current_time = ctime()
        self.current_time = current_time.split(' ')
        self.current_time[4] = self.current_time[4].split(':')
        self.output_msg = [f'[From うんちbot]\nｳﾝﾁﾌﾞﾘﾌﾞﾘ~💩ﾃﾞｰﾀﾖ~\n💩ﾃﾞ~ﾀ {current_time}\n\n#うんちbot']

    def makeAPI(self):
        """Return tweepy.API object"""
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        
        return tweepy.API(auth)

    def run(self):
        self.set_msg()
        if self.init_time[4][0] != self.current_time[4][0]:
            self.makeAPI().update_status(self.output_msg[0])
            self.init_time = self.current_time