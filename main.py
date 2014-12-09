from flask import Flask, render_template, request, session, url_for, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import *
from flask_bootstrap import Bootstrap
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app = Flask(__name__)
app.debug = True
app.secret_key = 'whoisduleyanddorjee'
db = SQLAlchemy(app)

# controllers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
