SkillConnection
===============

> CS365 Final Project

### main.py

  * studentCreate 

    Pass id, name, email, and an array of the skills
    
    Creates a student in the database and each skill in the skill table connected to the student.
    
   
  * jobCreate
  
    Pass id, title, name, email, phone, and an array of the skills.
    
    Creates a job in the database and each skill in the skill table connected to the job.
    
  *StudentSearch
  
    Pass student id.
    
    Returns an array of the 3 job ids that match the skills best.*
    
  * jobQuery
  
    Pass job id.
    
    Returns an array = [title, company, name, email, phone]
    
  * studentQuery
  
    Pass student id.
    
    Returns an array = [name, email]
    

 ### models.py

  4 Tables:
  
    * Student
    
    * Job
    
    * Skill - The point of this table is that it is easier to search matching skills using this seperate table and also allows for as many skills as we want. The Student and Job tables now don't have skills in them, the skills are added and linked during studentCreate and jobCreate.
    
    * Connection
    
  Also creates the database when run - probably should be changed later, but works fine now.
