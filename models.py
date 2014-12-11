import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Student(Base):
    __tablename__ = 'student'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    student_skill1 = Column(String(250), nullable=True)
    student_skill2 = Column(String(250), nullable=True)
    student_skill3 = Column(String(250), nullable=True)

class Job(Base):
    __tablename__ = 'job'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    jobTitle = Column(String(250), nullable=False, unique=True)
    employerName = Column(String(250), nullable=False)
    employerPhone = Column(Integer, unique=True)
    job_skill1 = Column(String(250), nullable=False)
    job_skill2 = Column(String(250), nullable=False)
    job_skill3 = Column(String(250), nullable=False)

class Connection(Base):
    __tablename__ = 'connection'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    job_id = Column(Integer, ForeignKey('job.id'))
    skillMatches = Column(String(250))
    student = relationship(Student)
    job = relationship(Job)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///connection.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)