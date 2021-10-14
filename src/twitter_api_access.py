import requests
import os
import traceback
import sys

# WINDOWS path , we can change to any code location
code_path = "C:\\Users\\RAMA\\Desktop\\python\\playground\\anymind_project"
sys.path.insert(0, f"{code_path}")


class TwitterApiAccess():
    def __init__(self, cfg):
        self.cfg = cfg

    def bearer_oauth(self, r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {self.cfg.bearer_token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r

    def get_tweets_by_hashtag(self, hashtag, limit):
        '''
        Two major tasks performing here
        1 -  Get the list of recent tweets from twitter using twitter api
        2 -  Filter tweets from step 1 with hashtag specific
        '''

        query_params = {
            'query': '(from:twitterdev -is:retweet) OR #twitterdev',
            'tweet.fields': 'author_id'
        }

        response = requests.get(self.cfg.twitter_search_api, auth=self.bearer_oauth, params=query_params, verify=False)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        # filter only requested hashtags tweets
        tweets = response.json()["data"]
        print(type(tweets))
        response_ = {"data": []}

        i = 1
        for tweet in tweets:
            if f"#{hashtag}" in tweet["text"]:
                if i <= limit:
                    response_["data"].append(tweet)
                    i += 1
                else:
                    break

        return response_, response.status_code

    def get_users_tweets(self, user, limit):
        '''
        Three major tasks performing here
        1 - Get user information from twitter api by username
        2 - from above response , get the userid
        3 - Finally call the twitter api by using userid and get the user specific tweets
        '''

        self.cfg.twitter_by_username_api += f"/{user}"
        response = requests.get(self.cfg.twitter_by_username_api, auth=self.bearer_oauth, verify=False)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        user_id = response.json()["data"]["id"]
        query_params = {
            'max_results': limit
        }

        self.cfg.twitter_by_id_api = self.cfg.twitter_by_id_api.format(user_id)
        response = requests.get(self.cfg.twitter_by_id_api, auth=self.bearer_oauth, params=query_params, verify=False)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response
