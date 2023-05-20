from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from quiz_questions.quiz_data_master import *
from customer_questions import initCustomerQuestions
from flask_cors import CORS
"""
These object can be used throughout project.
1.) Objects from this file can be included in many blueprints
2.) Isolating these object definitions avoids duplication and circular dependencies
"""

# Setup of key Flask object (app)
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
# Setup SQLAlchemy object and properties for the database (db)
dbURI = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)

@app.before_first_request
def activate_job():
    initCustomerQuestions()

@app.before_first_request
def activate_job():
    quiz_data_master.init()
    quiz_data_master.keepUpdating()
    
