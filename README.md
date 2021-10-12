# CustomerFeedbackSystem  
A customer feedback system using Flask in the Frontend and MySQL DB.  
Built to be hosted on AWS ELB and AWS RDS.  
Uses mailtrap to send HTML based text to the specified mailtrap account(send_mail.py)

***How to run and deploy***  
  - Run the rds.py to initialize the database
  - Follow the steps in DB.txt to create database
  - Extract the endpoint of the RDS and insert it in SQLALCHEMY_DATABASE_URI in feedbackapp/application.py
  - Create and ELB python application and upload the feedback app as a zip file
  - *Done!*
  
