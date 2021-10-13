import requests

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAMdFUgEAAAAAEhKVjpccRjOJIFgP9%2Bo7pWdUjnU%3DKF7P1nh9Pwb6orm2DVpBblxTgCjOzxwPoJ7SfBCLGh6GpjPMJA"
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def get_tweets_by_hashtag(hashtag, limit):
    query_params = {
        'query': '(from:twitterdev -is:retweet) OR #twitterdev',
        'tweet.fields': 'author_id',
        'max_results': limit
    }
    url = "https://api.twitter.com/2/tweets/search/recent"
    response = requests.get(url, auth=bearer_oauth, params=query_params, verify=False)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_users_tweets(limit):
    query_params = {
        'query': '(from:twitterdev -is:retweet) OR #twitterdev',
        'tweet.fields': 'author_id',
        'max_results': limit
    }
    url = "https://api.twitter.com/2/tweets/search/recent"
    response = requests.get(url, auth=bearer_oauth, params=query_params, verify=False)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()