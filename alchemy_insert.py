from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import Student, Job, Connection, Base
 
engine = create_engine('sqlite:///connection.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
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
 
# Insert a Student in the student table
new_student = Student(id=123, first_name='lucas', last_name='duley', email='dulelu01@luther.edu', student_skill1='ijiji', student_skill2='sdfsdf', student_skill3='sjkij')
session.add(new_student)
session.commit()
 
# Insert an job in the job table
new_job = Job(id=890, jobTitle='Cook', employerName='Bob', employerPhone=8908980, job_skill1='jjii', job_skill2='jijidf', job_skill3='uiuiu')
session.add(new_job)
session.commit()