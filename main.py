from flask import Flask, render_template, request, session, url_for, jsonify, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import *
from flask_bootstrap import Bootstrap
import os

from models import Student, Job, Base, Skill
from sqlalchemy import create_engine
engine = create_engine('sqlite:///connection.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from collections import Counter

DBSession = sessionmaker()
DBSession.bind = engine

app = Flask(__name__)
app.debug = True
app.secret_key = 'whoisduleyanddorjee'

Bootstrap(app)

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
		session.add(new_skill)
		# Section added

	session.commit()

	return new_jid

# Pass student id
# Gets skills from Skill table
# Searches for skills in job_id items
# Counter() counts them and puts them from most common to least
# Returns the job_ids of the 3 best fits in an array
def jobMatch(sid):
	session = DBSession()

	skill_list = []
	q = session.query(Skill).filter(Skill.student_id == sid).all()
	for b in q:
		skill_list.append(b.skill)
	tally = []
	for skill in skill_list:
		s = session.query(Skill).filter(Skill.skill == skill, Skill.job_id).all()
		for c in s:
			j = session.query(Job).filter(Job.id == c.job_id).one()
			tally.append(c.job_id)
	most_common = Counter(tally).most_common()
	result = []
	try:
		result.append(most_common[0][0])
	except IndexError:
		result.append(1)
	try:
		result.append(most_common[1][0])
	except IndexError:
		result.append(1)
	try:
		result.append(most_common[2][0])
	except IndexError:
		result.append(1)

	return result

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

def findJobid(name):
	session = DBSession()

	q = session.query(Job).filter(Job.name == name).one()
	return q.id

def getStudentSkills(sid):
	session = DBSession()
	skillArray = []
	items = session.query(Skill).filter(Skill.student_id == sid).all()
	for i in items:
		skillArray.append(i.skill)
	return skillArray

def getJobSkills(jid):
	session = DBSession()
	skillArray = []
	items = session.query(Skill).filter(Skill.job_id == jid).all()
	for i in items:
		skillArray.append(i.skill)
	return skillArray

#Forms
class SkillForm(Form):
	skill = TextField('Skill')

class NewStudentForm(Form):
	firstname = TextField('First Name')
	lastname = TextField('Last Name')
	email = TextField('E-mail')
	phone = TextField('Phone Number')

	skill1 = SelectField('Skill 1', choices=[('Programming','Programming'), ('Communication','Communication'),('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer Service', 'Customer Service')])
	skill2 = SelectField('Skill 2', choices=[('Leadership','Leadership'),('Spanish','Spanish'),('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer Service', 'Customer Service')])
	skill3 = SelectField('Skill 3', choices=[('Spanish','Spanish'),('Team Work','Team Work'),('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer Service', 'Customer Service')])

class StudentSearch(Form):
	name = TextField('Name of Student')

class NewJobForm(Form):
	firstname = TextField('First Name')
	lastname = TextField('Last Name')
	email = TextField('Email')
	phone = TextField('Phone Number')
	company = TextField('Company')
	title = TextField('Job Title')

	skill1 = SelectField('Skill 1', choices=[('Programming','Programming'), ('Communication','Communication'),('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer Service', 'Customer Service')])
	skill2 = SelectField('Skill 2', choices=[('Programming','Programming'), ('Communication','Communication'),('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer Service', 'Customer Service')])
	skill3 = SelectField('Skill 3', choices=[('Programming','Programming'), ('Communication','Communication'),('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer Service', 'Customer Service')])

class JobSearch(Form):
	name = TextField('Employer Name')

# controllers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#Routes
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/students')
def studentsearch():
	form = StudentSearch()
	if 'name' in request.args: 
		name = request.args['name']

		try:
			sid = findStudentid(name)
			sid = str(sid)
			full_url = url_for('sprofile', sid=sid)
			return redirect(full_url)
		except NoResultFound:
			return render_template('student.html', form=form)
	return render_template('student.html', form=form)

@app.route('/sprofile/<sid>')
def sprofile(sid):
	studentInfo = studentQuery(sid)
	name = studentInfo[0].split()
	first = name[0].capitalize()
	last = name[1].capitalize()
	name = first + " " + last
	skillInfo = getStudentSkills(sid)

	idArray = jobMatch(sid)
	employerName = studentQuery(sid)[0]
	jobNameArray = []
	jobTitleArray = []
	for i in idArray:
		jobNameArray.append(jobQuery(i)[2])
		jobTitleArray.append(jobQuery(i)[0])

	return render_template('sprofile.html', name=name, studentInfo=studentInfo, skillInfo=skillInfo, jobNameArray=jobNameArray, jobTitleArray=jobTitleArray, employerName=employerName)

@app.route('/jprofile/<jid>')
def jprofile(jid):
	jobInfo = jobQuery(jid)
	name = jobInfo[2].split()
	first = name[0].capitalize()
	last = name[1].capitalize()
	name = first + " " + last
	skillInfo = getJobSkills(jid)
	return render_template('jprofile.html', name=name, jobInfo=jobInfo, skillInfo=skillInfo)

@app.route('/jobs')
def jobsearch():
	form = JobSearch()
	if 'name' in request.args:
		name = request.args['name']
		try:
			jid = findJobid(name)
			jid = str(jid)
			full_url = url_for('jprofile', jid=jid)
			return redirect(full_url)
		except NoResultFound:
			return render_template('job.html', form=form)
	return render_template('job.html', form=form)

# @app.route('/top3/<sid>')
# def top3search(sid):
# 	jobArray = jobMatch(sid)
# 	name = studentQuery(sid)[2]
# 	return render_template('top3.html', jobArray=jobArray, name=name)

@app.route('/newjob')
def newjob():
	form = NewJobForm()
	if 'firstname' in request.args:
		firstname = request.args['firstname']
		firstname = firstname.lower()
		lastname = request.args['lastname']
		lastname = lastname.lower()
		name = firstname + " " + lastname		
		email = request.args['email']
		phone = request.args['phone']
		company = request.args['company']
		title = request.args['title']

		skill1 = request.args['skill1']
		skill2 = request.args['skill2']
		skill3 = request.args['skill3']
		skillArray = []
		skillArray.append(skill1)
		skillArray.append(skill2)
		skillArray.append(skill3)

		jid = jobCreate(title, company, name, email, phone, skillArray)
		full_url = url_for('jprofile', jid=jid)
		return redirect(full_url)

	else:
		return render_template('newjob.html', form=form)

@app.route('/newstudent')
def newstudent():
	form = NewStudentForm()
	if 'firstname' in request.args:
		firstname = request.args['firstname']
		firstname = firstname.lower()
		lastname = request.args['lastname']
		lastname = lastname.lower()
		name = firstname + " " + lastname		
		email = request.args['email']
		phone = request.args['phone']

		skill1 = request.args['skill1']
		skill2 = request.args['skill2']
		skill3 = request.args['skill3']
		skillArray = []
		skillArray.append(skill1)
		skillArray.append(skill2)
		skillArray.append(skill3)

		sid = studentCreate(name, email, phone, skillArray)
		full_url = url_for('sprofile', sid=sid)
		return redirect(full_url)

	else:
		return render_template('newstudent2.html', form=form)


if __name__ == '__main__':
	app.run()
