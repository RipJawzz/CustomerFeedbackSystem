from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
application=Flask(__name__)


db_endpoint='feedback2.cxnsb6fwzses.us-east-1.rds.amazonaws.com'
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:feedback@'+db_endpoint+'/flask_app'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.debug = False
db = SQLAlchemy(application)

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
        data = Feedback(customer,dealer,rating,comments)
        db.session.add(data)
        db.session.commit()
        send_mail(customer,dealer,rating,comments)
        return  render_template('success.html')
      

        return render_template('success.html',)


if __name__=='__main__':
    application.run()
