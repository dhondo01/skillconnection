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

# GET IS BEAUTIFUL
# q = session.query(Student)
# print(q.get(2).name)
def jobCreate(title, company, name, email, phone, skill_list):
	session = DBSession()
	j_ordered = session.query(Job).order_by(-Job.id)
	new_jid = j_ordered.first().id + 1

	sk_ordered = session.query(Skill).order_by(-Skill.id)
	new_skid = sk_ordered.first().id + 1

	new_job = Job(id=new_jid, title=title, company=company, email=email, phone=phone, name=name)
	session.add(new_job)

	for skill in skill_list:
		new_skill = Skill(id=new_skid, job_id=new_jid, skill=skill)
		new_skid += 1
		session.add(new_job)
		# Section added

	session.commit()

	return new_jid

def jobQuery(jid):
	session = DBSession()

	result = []
	q = session.query(Job).filter(Job.id == jid).one()
	result.append(q.title)
	result.append(q.company)
	result.append(q.name)
	result.append(q.email)
	result.append(q.phone)

	return result 

def findJobid(name):
	session = DBSession()

	q = session.query(Job).filter(Job.name == name).one()
	return q.id

def getJobSkills(jid):
	session = DBSession()
	skillArray = []
	items = session.query(Skill).filter(Skill.job_id == jid).all()
	for i in items:
		skillArray.append(i.skill)
	return skillArray

jid = jobCreate('aeefe', 'sdfcv', 'haha dada', '123153', '8686', ['jklj', 'jiljilkkl', 'jijdhdhd'])
print(getJobSkills(jid))
