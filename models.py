from main import db

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), index=True, unique=False)
	last_name = db.Column(db.String(64), index=True, unique=False)
	email = db.Column(db.String(120), index=True, unique=True)
	student_skill1 = db.Column(db.String(64), index=True, unique=False)
	student_skill2 = db.Column(db.String(64), index=True, unique=False)
	student_skill3 = db.Column(db.String(64), index=True, unique=False)

	def __repr__(self):
		return '<Student %r>' % (self.email)

# class Job(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	jobTitle = db.Column(db.String(64), index=True, unique=True)
# 	employerName = db.Column(db.String(64), index=True, unique=False)
# 	employerPhone = db.Column(db.Integer(120), index=True, unique=True)
# 	job_skill1 = db.Column(db.String(64), index=True, unique=False)
# 	job_skill2 = db.Column(db.String(64), index=True, unique=False)
# 	job_skill3 = db.Column(db.String(64), index=True, unique=False)

# 	def __repr__(self):
# 		return '<Post %r>' % (self.jobTitle)

# class Connection(db.Model):
# 	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
# 	job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
# 	skillMatches = db.Column(db.String(64))

# 	def __repr__(self):
# 		return '<Post %r>' % (self.skillMatches)