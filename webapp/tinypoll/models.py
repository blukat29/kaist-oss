import datetime
from tinypoll import app, db
from .arcus_client import Arcus, ArcusLocator, ArcusMCNodeAllocator, ArcusTranscoder

class Poll(db.Model):
    __tablename__ = 'poll'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    created_at = db.Column(db.DateTime)
    options = db.relationship('Option', backref='poll', lazy='dynamic')

    def __init__(self, title, id=None):
        self.title = title
        self.created_at = datetime.datetime.utcnow()
        self.id = id

class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))
    text = db.Column(db.String(100))
    votes = db.Column(db.Integer)

    def __init__(self, text):
        self.text = text
        self.votes = 0

def get_arcus_client():
    zk = app.config['ARCUS_ZK_ADDRESS']
    code = app.config['ARCUS_SERVICE_CODE']
    client = Arcus(ArcusLocator(ArcusMCNodeAllocator(ArcusTranscoder())))
    client.connect(zk, code)
    return client

if app.config['USE_ARCUS']:
    arcus = get_arcus_client()

def options_basic(options):
    pass

def options_arcus(options):
    for option in options:
        key = "option:%d" % option.id
        ret = arcus.get(key).get_result()
        if ret:
            option.votes = ret
        else:
            arcus.set(key, option.votes)

def vote_basic(option_id):
    option = Option.query.get(option_id)
    option.votes += 1
    db.session.commit()

def vote_arcus(option_id):
    key = "option:%d" % option_id
    ret = arcus.get(key).get_result()
    if not ret:
        arcus.set(key, 1)
    else:
        incrd = arcus.set(key, ret+1)

if app.config['USE_ARCUS']:
    vote = vote_arcus
    get_options = options_arcus
else:
    vote = vote_basic
    get_options = options_basic
