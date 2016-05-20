import datetime
from tinypoll import db

class Poll(db.Model):
    __tablename__ = 'poll'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    created_at = db.Column(db.DateTime)
    options = db.relationship('Option', backref='poll', lazy='dynamic')

    def __init__(self, title):
        self.title = title
        self.created_at = datetime.datetime.utcnow()

class Option(db.Model):
    __tablename__ = 'option'
    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))
    text = db.Column(db.String(100))
    votes = db.Column(db.Integer)

    def __init__(self, text):
        self.text = text
        self.votes = 0