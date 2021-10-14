'''
   unit tests for twitter api methods
'''
import pytest
from src.twitter_api_access import TwitterApiAccess
from src.utilities import Config


class TestTwitterApiAccess:

    def test_get_tweets_by_hashtag(self):
        hashtag, limit = "Python", 20
        cfg = Config()
        _, status_code = TwitterApiAccess(cfg).get_tweets_by_hashtag(hashtag, limit)
        assert status_code == 200

    def test_get_users_tweets(self):
        user, limit = "dummyUser", 20
        cfg = Config()
        r = TwitterApiAccess(cfg).get_users_tweets(user, limit)
        assert r.status_code == 200

    def test_get_tweets_by_hashtag_invalid_url(self):
        hashtag, limit = "Python", 20
        cfg = Config()
        cfg.twitter_search_api = "http://dummy_url"
        try:
            TwitterApiAccess(cfg).get_tweets_by_hashtag(hashtag, limit)
            assert False
        except:
            assert True

    def test_get_users_tweets_invalid_url(self):
        user, limit = "dummyUser", 20
        cfg = Config()
        cfg.twitter_by_id_api = "http://dummy_url"
        try:
            r = TwitterApiAccess(cfg).get_users_tweets(user, limit)
            assert False
        except:
            assert True

    def test_get_tweets_by_hashtag_404_error(self):
        hashtag, limit = "Python", 20
        cfg = Config()
        cfg.twitter_search_api += 'DUMMY'

        try:
            TwitterApiAccess(cfg).get_tweets_by_hashtag(hashtag, limit)
            assert False
        except Exception as err:
            assert err.args[0] == 404

    def test_get_users_tweets_404_error(self):
        user, limit = "dummyUser", 20
        cfg = Config()
        cfg.twitter_by_id_api += 'DUMMY'

        try:
            r = TwitterApiAccess(cfg).get_users_tweets(user, limit)
            assert False
        except Exception as err:
            assert err.args[0] == 404
