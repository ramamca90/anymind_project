'''
        -- FLASK REST API --
    ** It has below end points **
    1 - Get tweets by a hashtag - return the list of tweets with the given hashtag.
        sample request
        curl -H "Accept: application/json" -X GET http://localhost:5000/hashtags/<sample_hashtag>?limit=40
        sample_hashtag -> Python or Java ..
    2 - Get user tweets - return the list of tweets that the user has on his feed in JSON format.
        sample request
        curl -H "Accept: application/json" -X GET http://localhost:5000/users/<sample_username>?limit=20
        sample_username -> twitter or smith ..

'''
import os
import sys
import traceback

from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

# WINDOWS path , we can change to any code location
code_path = "C:\\Users\\RAMA\\Desktop\\python\\playground\\anymind_project"
sys.path.insert(0, f"{code_path}")

from src.security import authenticate, identity
from src.utilities import Config, get_logger
from src.twitter_api_access import TwitterApiAccess as twitter


def create_logger(cfg):
    '''
    It will create logger for logging information
    '''

    log_loc = cfg.logfile_location
    today_ts = datetime.now().strftime("%Y%m%d")
    log_file = f"{log_loc}\\twitter_api_{today_ts}.log"

    return get_logger(log_file, log_name='twitter_rest_api')


def create_flask_app():
    '''
    It will create a flask api
    '''

    cfg = Config()
    logger_, file_handler = create_logger(cfg)

    APPLICATION = Flask(__name__)
    # To allow flask propagating exception even if debug is set to false on APPLICATION
    APPLICATION.config['PROPAGATE_EXCEPTIONS'] = True
    APPLICATION.secret_key = cfg.app_key
    APPLICATION.logger.addHandler(file_handler)

    api = Api(APPLICATION)

    jwt = JWT(APPLICATION, authenticate, identity)  # /auth

    APPLICATION.config['DEBUG'] = True

    class HashTag(Resource):
        #@jwt_required
        def get(self, hashtag):
            '''
            Return the list of tweets with the given <hashtag>
            '''

            limit = request.args.get('limit', default=30, type=int)
            logger_.info("Getting tweets by hashtags")

            response, status_code = twitter(cfg).get_tweets_by_hashtag(hashtag, limit)
            return response, status_code

    class Users(Resource):
        #@jwt_required
        def get(self, user_name):
            '''
            Return the list of tweets that the user(user_name) has on his feed in JSON format.
            '''
            limit = request.args.get('limit', default=30, type=int)
            logger_.info("Getting tweets by users")

            r = twitter(cfg).get_users_tweets(user_name, limit)
            return r.json()

    api.add_resource(HashTag, '/hashtags/<string:hashtag>')
    api.add_resource(Users, '/users/<string:user_name>')

    return APPLICATION, logger_


if __name__ == '__main__':
    try:
        APPLICATION, logger_ = create_flask_app()
        APPLICATION.run(port=5000)
    except:
        logger_.critical(traceback.format_exc())
