""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json
from quiz_questions.quiz_data_master import quiz_data_master

from __init__ import app, db
from sqlalchemy.exc import *
from werkzeug.security import generate_password_hash, check_password_hash
''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''
# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
    
class Question(db.Model):
    __tablename__ = 'questions'   
    id = db.Column(db.Integer, primary_key=True)    
    _subject = db.Column(db.String(255), unique=False, nullable=False)   
    _timestamp = db.Column(db.Date)
    qid = db.Column(db.String, unique=False, nullable=False)    
    pinned =  db.Column(db.Integer, unique=False, nullable=True)    
    question =  db.Column(db.Text, unique=False, nullable=True) 
    answer =  db.Column(db.Text, unique=False, nullable=True)   

    def __init__(self, subject, qid, question, answer, pinned, ts=date.today()):
        self.question = question        
        self.qid = qid        
        self.answer = answer
        self._subject = subject           
        self._timestamp = ts    
        self.pinned = pinned

    @property
    def subject(self):
        return self._subject    
    @subject.setter
    def subject(self, s):
        self._subject = s    
    
    @property
    def timestamp(self):
        ts_string = self._timestamp.strftime('%m-%d-%Y')
        return ts_string    # dob should be have verification for type date
    @timestamp.setter
    def timestamp(self,ts):
        self._timestamp = ts      

    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except SQLAlchemyError as e:             
            print(e)
        except IntegrityError:
            db.session.remove()
            return None    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "timestamp": self.timestamp,
            "question": self.question,
            "answer": self.answer,
            "pinned": self.pinned,
            #"questions": [question.read() for question in self.questions]
        }    # CRUD update: 
    # returns self
    def update(self, s="", ts="", pinned=0):
        """only updates values with length"""
        if len(s) > 0:
            self.subject = s        
        if len(ts) > 0:
            self.timestamp = ts
        
        self.pinned = pinned
        db.session.commit()
        return self    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
        """Database Creation and Testing """
        # Builds working data for testing

    @staticmethod
    def getById(id):        
        recs = db.session.query(Question).filter(Question.id == id)
        for r in recs:
            # Should be just 1 rec matched
            return r        
        return None
    @staticmethod
    def getAll():
        allQs = Question.query.all()
        rsp = []
        pins = []
        for qz in allQs:            
            q = qz.read()
            if (qz.pinned == 0 ):
                rsp.append(q)
            else:                
                pins.append(q)
    
        return pins + rsp

def initQuestions():
    quiz_data_master.init()
    quizes = quiz_data_master.get_all_questions()

    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
                
        """Builds sample user/note(s) data"""        
        for quiz in quizes:
            
            s = quiz["subject"]
            qid = quiz["id"]
            question = quiz["question"]
            answer = quiz["answer"]
            pinned = quiz["pinned"]
            qz = Question(subject=s, qid=qid, question=question, answer=answer, pinned=pinned)            
            try:
                q = qz.create()

            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {qz.subject}")
        
    # quizAll = Question.query.all()    
    #for qz in quizAll:
    #    print(qz.subject + qz.timestamp)


 