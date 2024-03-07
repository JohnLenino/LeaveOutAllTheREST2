import flask
from flask import request, jsonify, make_response

from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')

@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs)
    print(type(jobs))
    return jsonify(
        {'jobs': [item.to_dict(only=('title', 'wealth')) for item in jobs]})
