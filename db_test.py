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
def studentCreate(name, email, phone, skill_list):
	session = DBSession()
	s_ordered = session.query(Student).order_by(-Student.id)
	new_sid = s_ordered.first().id + 1

	sk_ordered = session.query(Skill).order_by(-Skill.id)
	new_skid = sk_ordered.first().id + 1

	new_student = Student(id=new_sid, name=name, email=email, phone=phone)
	session.add(new_student)

	# Pass an array of skills
	for skill in skill_list:
		new_skill = Skill(id=new_skid, student_id=new_sid, skill=skill)
		new_skid += 1
		session.add(new_skill)

	session.commit()

	return new_sid

def studentQuery(sid):
	session = DBSession()

	result = []
	q = session.query(Student).filter(Student.id == sid).one()
	result.append(q.name)
	result.append(q.email)
	result.append(q.phone)

	return result

def findStudentid(name):
	session = DBSession()

	q = session.query(Student).filter(Student.name == name).one()
	return q.id

def getStudentSkills(sid):
	session = DBSession()
	skillArray = []
	items = session.query(Skill).filter(Skill.student_id == sid).all()
	for i in items:
		skillArray.append(i.skill)
	return skillArray

sid = studentCreate('jack bauer', 'jijil', '7856', ['jklj', 'jiljilkkl', 'jijdhdhd'])
print(getStudentSkills(sid))
