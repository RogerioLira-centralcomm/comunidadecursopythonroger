from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '2aa46adc90870490d94b48bce60b0239'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidades.db'

database = SQLAlchemy(app)

from comunidadeimpressionadora import routes