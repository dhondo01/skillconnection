from flask import Flask, render_template, request, session, url_for, jsonify, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import *
from flask_bootstrap import Bootstrap
import os

from models import Student, Job, Connection, Base, Skill
from sqlalchemy import create_engine
engine = create_engine('sqlite:///connection.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
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

	new_student = Student(id=new_sid, name=name, email=email)
	session.add(new_student)

	# Pass an array of skills
	for skill in skill_list:
		new_skill = Skill(id=new_skid, student_id=new_sid, skill=skill)
		new_skid += 1

	session.commit()

	return jobSearch(new_sid)

def jobCreate(title, company, name, email, phone, skill_list):
	session = DBSession()
	j_ordered = session.query(Job).order_by(-Job.id)
	new_jid = j_ordered.first().id + 1

	sk_ordered = session.query(Skill).order_by(-Skill.id)
	new_skid = sk_ordered.first().id + 1

	new_job = Job(id=new_jid, title=title, company=company, email=email, phone=phone)
	session.add(new_job)

	for skill in skill_list:
		new_skill = Skill(id=new_skid, job_id=new_jid, skill=skill)
		new_skid += 1

	session.commit()	

# Pass student id
# Gets skills from Skill table
# Searches for skills in job_id items
# Counter() counts them and puts them from most common to least
# Returns the job_ids of the 3 best fits in an array
def jobSearch(sid):
	session = DBSession()

	skill_list = []
	q = session.query(Skill).filter(Skill.student_id == sid).all()
	for b in a:
		skill_list.append(b.skill)
	tally = []
	for skill in skill_list:
		s = session.query(Skill).filter(Skill.skill == skill, Skill.job_id).all()
		for c in s:
			j = session.query(Job).filter(Job.id == c.job_id).one()
			tally.append(c.job_id)
	most_common = Counter(tally).most_common()
	result = []
	result.append(most_common[0][0])
	result.append(most_common[1][0])
	result.append(most_common[2][0])

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

def getStudentSkills(sid):
	session = DBSession()
	skillArray = []
	items = session.query(Skill).filter(Skill.student_id == sid).all()
	for i in items:
		skillArray.append(i.skill)
	return skillArray

#Forms
class SkillForm(Form):
	skill = TextField('Skill')

class NewStudentForm(Form):
	name = TextField('Name of Student')
	email = TextField('Email')
	phone = TextField('Phone Number')

	skill1 = SelectField('Skill', choices=[('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer', 'Customer Service')])
	skill2 = SelectField('Skill', choices=[('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer', 'Customer Service')])
	skill3 = SelectField('Skill', choices=[('Cashier','Cashier'), ('Dishwashing', 'Dishwashing'), ('Customer', 'Customer Service')])

class StudentSearch(Form):
	name = TextField('Name of Student')

class JobForm(Form):
	job = TextField('Job')



# controllers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#Routes
@app.route('/')
def home():
	return render_template('home.html')


@app.route('/skills')
def skillsearch():
	form = SkillForm()
	# if request.args.get("skill") != None:
	return render_template('skill.html')

@app.route('/students')
def studentsearch():
	form = StudentSearch()
	if 'name' in request.args: 
		name = request.args['name']
		sid = findStudentid(name)
		sid = str(sid)
		
		full_url = url_for('sprofile', sid=sid)
		return redirect(full_url)
	return render_template('student.html', form=form)

@app.route('/sprofile/<sid>')
def sprofile(sid):
	studentInfo = studentQuery(sid)
	skillInfo = getStudentSkills(sid)
	return render_template('sprofile.html', studentInfo=studentInfo, skillInfo=skillInfo)

# # Search if student in db
# @app.route('/jobs')
# def jobsearch():
# 	form = StudentSearch()
# 	name = request.args['name']

# 	if findStudentid(name):
# 		sid = findStudentid(name)
# 		jobs = jobSearch(sid)

# 		# If they are, search result
# 		return render_template('job.html', form=form, jobs=jobs)
# 	# return newstudent
# 	else:
# 		return render_template('newstudent.html', form=form)

# @app.route('/newstudent')
# def newstudent():
# 	form = NewStudentForm()

# 	name = request.args['name']
# 	email = request.args['email']
# 	phone = request.args['phone']

# 	skill1 = request.args['skill1']
# 	skill2 = request.args['skill2']
# 	skill3 = request.args['skill3']
# 	skillArray = []
# 	skillArray.append(skill1)
# 	skillArray.append(skill2)
# 	skillArray.append(skill3)

# 	sid = studentCreate(name, email, phone, skillArray)
# 	jobs = jobSearch(sid)

# 	return render_template('job.html', jobs=jobArray)

if __name__ == '__main__':
	app.run()
