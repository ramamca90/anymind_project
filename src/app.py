import os

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity

from twitter_api_access import get_tweets_by_hashtag, get_users_tweets

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app

app.secret_key = 'Mayur'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

app.config['DEBUG'] = True

class HashTag(Resource):
    def get(self, hashtag):
        limit = request.args.get('limit', default=30, type=int)
        r = get_tweets_by_hashtag(hashtag, limit)
        return r

class Users(Resource):
    def get(self):
        limit = request.args.get('limit', default=30, type=int)
        r = get_users_tweets(limit)
        return r

api.add_resource(HashTag, '/hashtags/<string:hashtag>')
api.add_resource(Users, '/users/twitter')

if __name__ == '__main__':
    app.run(port=5000)