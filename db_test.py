from flask import Flask, render_template, request, session, url_for, jsonify, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import *
from flask_bootstrap import Bootstrap
from sqlalchemy.orm.exc import NoResultFound
import os

from models import Student, Job, Base, Skill
from sqlalchemy import create_engine
engine = create_engine('sqlite:///connection.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
from collections import Counter

app = Flask(__name__)
app.debug = True
app.secret_key = 'whoisduleyanddorjee'
session = DBSession()
# Make a query to find all Persons in the database
# session.query(Job).all()
# Return the first Person from all Persons in the database
# job = session.query(Job).first()
# print(job.name)
# student = session.query(Student).first()
# print(student.first_name)
# Find all Address whose person field is pointing to the person object
# session.query(Address).filter(Address.person == person).all()
# # Retrieve one Address whose person field is point to the person object
# session.query(Address).filter(Address.person == person).one()
# address = session.query(Address).filter(Address.person == person).one()
# address.post_code

name = "Lucas Duley"
name = name.lower()

print(name)
