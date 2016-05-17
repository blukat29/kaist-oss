from flask import Blueprint, render_template
from .models import Poll, Option

blueprint = Blueprint('tinypoll', __name__)

@blueprint.route('/')
def index():
    polls = Poll.query.all()
    return render_template("index.html", polls=polls)

@blueprint.route('/<int:poll_id>')
def poll(poll_id):
    poll = Poll.query.get(poll_id)
    options = Option.query.filter_by(poll_id=poll_id).all()
    return render_template("poll.html", poll=poll, options=options)
