from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import json
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:123@localhost:5432/trello'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    date_created = db.Column(db.Date())
    status = db.Column(db.String(100))

class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created')

@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

@app.cli.command('db_seed')
def db_seed():
    cards =[
        Card(
        title = 'Start the project',
        description = 'Stage 1 - ERD Creation',
        status = 'Done',
        date_created = date.today()
    ),

        Card(
        title = 'ORM Queries',
        description = 'Stage 2 - Implement CRUD queries',
        status = 'In progress',
        date_created = date.today()
    ),

        Card(
        title = 'Marshmallow',
        description = 'Stage 3 - Implement JSONify of models',
        status = 'In progress',
        date_created = date.today()
    )
    ]

    db.session.add_all(cards)
    db.session.commit()

    print('Database seeded')

@app.route('/cards')
def all_cards():
    # select * from cards;
    stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)
    

@app.route('/')
def index():
    return 'Hello, world'