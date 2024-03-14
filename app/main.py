from flask import Flask, make_response, jsonify
from data import db_session, jobs_api, news_api
from flask_restful import reqparse, abort, Api, Resource
from data import users_resource


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


app = Flask(__name__)
api = Api(app)

@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/blogs.db")
    # app.register_blueprint(jobs_api.blueprint)
    # app.register_blueprint(news_api.blueprint)
    # app.register_blueprint(users_api.blueprint)
    api.add_resource(users_resource.UsersListResource, '/api/v2/user')

    # для одного объекта
    api.add_resource(users_resource.UsersResource, '/api/v2/user/<int:user_id>')
    app.run()


if __name__ == '__main__':
    main()
