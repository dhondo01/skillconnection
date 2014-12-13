from models import Student, Job, Connection, Base, Skill
from sqlalchemy import create_engine
from collections import Counter
engine = create_engine('sqlite:///connection.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
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
