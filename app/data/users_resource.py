from . import db_session
from datetime import datetime
from .users import User
from flask_restful import abort, Resource, reqparse
from flask import jsonify, make_response


parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('about', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)
parser.add_argument('created_date', required=True, type=datetime)

def abort_if_user_not_found(news_id):
    session = db_session.create_session()
    news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        news = session.query(User).get(user_id)
        if not news:
            return make_response(jsonify({'error': 'Not found'}), 404)
        return jsonify({'news': news.to_dict(
            only=('name', 'about', 'email', 'hashed_password', 'created_date'))})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'about', 'email', 'hashed_password', 'created_date')) for item in news]})
