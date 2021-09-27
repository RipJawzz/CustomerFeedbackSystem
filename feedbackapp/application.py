from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
application=Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    application.debug = True
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:013210@localhost/lexus'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db= SQLAlchemy(application)
else:
    '''application.config['MYSQL_HOST'] = 'feedback2.cxnsb6fwzses.us-east-1.rds.amazonaws.com'
    application.config['MYSQL_USER'] = 'admin'
    application.config['MYSQL_PASSWORD'] = 'feedback'
    application.config['MYSQL_DB'] = 'flask_app'
    '''
    application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:feedback@feedback2.cxnsb6fwzses.us-east-1.rds.amazonaws.com/flask_app'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #db = MySQLdb.connect(host="feedbackdb.cxnsb6fwzses.us-east-1.rds.amazonaws.com",port=3306,user="admin",passwd="feedback",db="flask_app",autocommit=True,use_unicode=True)
    application.debug = False
    db = SQLAlchemy(application)




#Postgresql init
class Feedback(db.Model):
    __tablename__ = 'feedback'
    customer = db.Column(db.String(200),primary_key=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text)
    def __init__(self,customer,dealer,rating,comments):
        self.customer=customer
        self.dealer=dealer
        self.rating=rating
        self.comments=comments 

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        customer=request.form['customer']
        dealer=request.form['dealer']
        rating=request.form['rating']
        comments=request.form['comments']
        if customer=='' or  dealer=='':
            return render_template('index.html', message='Please fill required fields')
        #PostGres
        #if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
        data = Feedback(customer,dealer,rating,comments)
        db.session.add(data)
        db.session.commit()
        send_mail(customer,dealer,rating,comments)
        return  render_template('success.html')
        
        #MYSQL
        #conn = mysql.connect()
        #conn.execute(''' INSERT INTO feedback VALUES(%s,%s,%s,%s)''',(customer,dealer,rating,comments))
        '''conn.commit()
        send_mail(customer,dealer,rating,comments)
        conn.close()
        '''
        '''cursor = db.cursor()'''
        #query = ''' INSERT INTO feedback VALUES(%s,%s,%s,%s)''',(customer,dealer,rating,comments)
        '''cursor.execute(query)
        languages = cursor.fetchall()
        languages = [list(l) for l in languages]'''

        return render_template('success.html',)


if __name__=='__main__':
    application.run()