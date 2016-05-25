from flask import Blueprint, render_template, redirect, url_for
from .models import Poll, Option
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
    return render_template("poll.html", poll=poll, options=options)

@blueprint.route('/<int:poll_id>/<int:option_id>')
def option(poll_id, option_id):
    option = Option.query.get(option_id)
    option.votes += 1
    db.session.commit()
    return redirect(url_for('tinypoll.index'))
