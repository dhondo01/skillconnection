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

student.drop(engine, checkfirst=True) 
student.create(engine, checkfirst=True)

job.drop(engine, checkfirst=True) 
job.create(engine, checkfirst=True)

connection.drop(engine, checkfirst=True) 
connection.create(engine, checkfirst=True)
# Insert a Student in the student table

# Insert an job in the job table
# When employers add jobs, have them enter their own skills and add those to a dropdown for students to choose from.

# Insert a Connection in the Connection table
new_job = Job(id=1, title='Sales Associate', company='JC Penny', name='Jacqueline Meyer', phone='(563)382-1192', email='penny@gmail.com', skill1='Cashier', skill2='Customer Service', skill3='Sales')
session.add(new_job)
new_job = Job(id=2, title='Hotel Front Desk', company='Quality Inn and Suites', name='Michael Douglas', phone='(563)867-5309', email='quality@yahoo.com', skill1='Customer Service', skill2='Computer Skills', skill3='Guest Services')
session.add(new_job)
new_job = Job(id=3, title='Construction Worker', company='Decorah Construction', name='Robert Bobson', phone='(563)382-5632', email='bobson123@gmail.com', skill1='Heavy Labor', skill2='Power Tools', skill3='Truck Driving')
session.add(new_job)
new_job = Job(id=4, title='Fast Food Worker', company='McDonalds', name='Rebecca Berger', phone='(563)382-7895', email='mickeyds@msn.com', skill1='Cashier', skill2='Customer Service', skill3='Dishwashing', skill4='Grill Operation')
session.add(new_job)

new_student = Student(id=1, name='lucas duley', email='dulelu01@luther.edu', skill1='Customer Service', skill2='Heavy Labor', skill3='Computer Skills')
session.add(new_student)
new_student = Student(id=2, name='bob robertson', email='robebo01@luther.edu', skill1='Grill Operation', skill2='Customer Service', skill3='Computer Skills')
session.add(new_student)
new_student = Student(id=3, name='jane doe', email='doeja02@luther.edu', skill1='Dishwashing', skill2='Heavy Labor', skill3='Computer Skills')
session.add(new_student)
session.commit()