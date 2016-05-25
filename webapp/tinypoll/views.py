from flask import Blueprint, render_template, redirect, url_for
from .models import Poll, Option, vote, get_options
from . import app, db

blueprint = Blueprint('tinypoll', __name__)

@blueprint.route('/')
def index():
    polls = Poll.query.all()
    return render_template("index.html", polls=polls)

@blueprint.route('/<int:poll_id>')
def poll(poll_id):
    poll = Poll.query.get(poll_id)
    options = Option.query.filter_by(poll_id=poll_id).all()
    get_options(options)
    return render_template("poll.html", poll=poll, options=options)

@blueprint.route('/<int:poll_id>/<int:option_id>')
def option(poll_id, option_id):
    vote(option_id)
    return redirect(url_for('tinypoll.poll', poll_id=poll_id))
