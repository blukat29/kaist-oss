#!/usr/bin/env python
import random
import string
from flask.ext.script import Manager
from tinypoll import app, db
from tinypoll.models import Poll, Option
import config

manager = Manager(app)

@manager.command
def run():
    """
    Run server
    """
    db.create_all()
    app.run("0.0.0.0", 5000)

@manager.command
def populate():
    """
    Populate database with sample data. All data are dropped.
    """
    charset = string.ascii_letters + string.digits
    def random_string():
        return ''.join([random.choice(charset) for _ in range(16)])

    POLL_COUNT = 10
    OPTION_MIN = 2
    OPTION_MAX = 6

    db.drop_all()
    db.create_all()

    for i in range(POLL_COUNT):
        p = Poll("poll_" + random_string())
        db.session.add(p)

        option_cnt = random.randint(OPTION_MIN, OPTION_MAX)
        for j in range(option_cnt):
            o = Option("opt_" + random_string())
            p.options.append(o)

        db.session.commit()

if __name__ == '__main__':
    manager.run()
