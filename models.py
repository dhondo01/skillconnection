import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()
 
class Student(Base):
    __tablename__ = 'student'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    phone = Column(String(250), nullable=False, unique=True)

class Job(Base):
    __tablename__ = 'job'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False, unique=True)
    company = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    phone = Column(String(250), unique=True, nullable=False)

class Skill(Base):
    __tablename__ = 'skill'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    job_id = Column(Integer, ForeignKey('job.id'))
    skill = Column(String(250), nullable=False)
    student = relationship(Student)
    job = relationship(Job)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///connection.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# When employers add jobs, have them enter their own skills and add those to a dropdown for students to choose from.

# Add jobs
new_job = Job(id=1, title='Sales Associate', company='JC Penny', name='jacqueline meyer', phone='(563)382-1192', email='penny@gmail.com')
session.add(new_job)
new_job = Job(id=2, title='Hotel Front Desk', company='Quality Inn and Suites', name='michael douglas', phone='(563)867-5309', email='quality@yahoo.com')
session.add(new_job)
new_job = Job(id=3, title='Construction Worker', company='Decorah Construction', name='robert bobson', phone='(563)382-5632', email='bobson123@gmail.com')
session.add(new_job)
new_job = Job(id=4, title='Fast Food Worker', company='McDonalds', name='rebecca berger', phone='(563)382-7895', email='mickeyds@msn.com')
session.add(new_job)
new_job = Job(id=5, title='Tech Helpdesk', company='LIS', name='carsten earl', phone='(533)382-5632', email='earcal@luther.edu')
session.add(new_job)
new_job = Job(id=6, title='French Tutor', company='French Department', name='madame feat', phone='(563)381-7895', email='feat@luther.edu')
session.add(new_job)
new_job = Job(id=7, title='Box Office', company='Campus Programming', name='bradley philips', phone='(563)381-5555', email='philbr01@luther.edu')
session.add(new_job)


# Add students
new_student = Student(id=1, name='lucas duley', email='dulelu01@luther.edu', phone='546-789-1232')
session.add(new_student)
new_student = Student(id=2, name='bob robertson', email='robebo01@luther.edu', phone='789-897-1234')
session.add(new_student)
new_student = Student(id=3, name='jane doe', email='doeja02@luther.edu', phone='789-837-1234')
session.add(new_student)
new_student = Student(id=4, name='dorjee dhondup', email='dhondo01@luther.edu', phone='515-837-1234')
session.add(new_student)

# Add job skills
new_skill = Skill(id=1, job_id=1, skill='Cashier')
session.add(new_skill)
new_skill= Skill(id=2, job_id=1, skill='Customer Service')
session.add(new_skill)
new_skill= Skill(id=3, job_id=1, skill='Sales')
session.add(new_skill)

new_skill = Skill(id=4, job_id=2, skill='Customer Service')
session.add(new_skill)
new_skill= Skill(id=5, job_id=2, skill='Computer Skills')
session.add(new_skill)
new_skill= Skill(id=6, job_id=2, skill='Guest Services')
session.add(new_skill)

new_skill = Skill(id=7, job_id=3, skill='Heavy Labor')
session.add(new_skill)
new_skill= Skill(id=8, job_id=3, skill='Power Tools')
session.add(new_skill)
new_skill= Skill(id=9, job_id=3, skill='Truck Driving')
session.add(new_skill)

new_skill = Skill(id=10, job_id=4, skill='Cashier')
session.add(new_skill)
new_skill= Skill(id=11, job_id=4, skill='Customer Service')
session.add(new_skill)
new_skill= Skill(id=12, job_id=4, skill='Dishwashing')
session.add(new_skill)
new_skill= Skill(id=13, job_id=4, skill='Grill Operation')

# Add student skills
new_skill = Skill(id=14, student_id=1, skill='Customer Service')
session.add(new_skill)
new_skill= Skill(id=15, student_id=1, skill='Heavy Labor')
session.add(new_skill)
new_skill= Skill(id=16, student_id=1, skill='Computer Skills')
session.add(new_skill)

new_skill = Skill(id=17, student_id=2, skill='Grill Operation')
session.add(new_skill)
new_skill= Skill(id=18, student_id=2, skill='Customer Service')
session.add(new_skill)
new_skill= Skill(id=19, student_id=2, skill='Computer Skills')
session.add(new_skill)

new_skill = Skill(id=20, student_id=3, skill='Dishwashing')
session.add(new_skill)
new_skill= Skill(id=21, student_id=3, skill='Heavy Labor')
session.add(new_skill)
new_skill= Skill(id=22, student_id=3, skill='Computer Skills')
session.add(new_skill)


new_skill = Skill(id=23, student_id=4, skill='Communication Skills')
session.add(new_skill)
new_skill= Skill(id=24, student_id=4, skill='French')
session.add(new_skill)
new_skill= Skill(id=25, student_id=4, skill='Customer Services')
session.add(new_skill)


new_skill= Skill(id=26, job_id=5, skill='Communication Skills')
session.add(new_skill)
new_skill= Skill(id=36, job_id=5, skill='MacBook')
session.add(new_skill)
new_skill= Skill(id=37, job_id=5, skill='Windows')
session.add(new_skill)


new_skill= Skill(id=27, job_id=6, skill='French')
session.add(new_skill)
new_skill= Skill(id=34, job_id=6, skill='Foreign Language')
session.add(new_skill)
new_skill= Skill(id=35, job_id=6, skill='History')
session.add(new_skill)

new_skill= Skill(id=32, job_id=7, skill='Communication Skills')
session.add(new_skill)
new_skill= Skill(id=33, job_id=7, skill='Ticket Selling')
session.add(new_skill)
new_skill=Skill(id=31, job_id=7, skill="Customer Services")
session.add(new_skill)


session.commit()

