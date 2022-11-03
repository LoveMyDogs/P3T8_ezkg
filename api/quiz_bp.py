from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
from flask import request
from quiz_questions.quiz_data_master import *

quiz_app_api = Blueprint('quiz_api_bp', __name__,
                   url_prefix='/api/quiz')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
quiz_api = Api(quiz_app_api)

class QuizAPI:
    # not implemented
    class _Get(Resource):
        def get(self, subject, totalQsInQuiz:int):
            return quiz_data_master.get_random_questions(subject, totalQsInQuiz)
            
    class _Read(Resource):
        def get(self):
            return jsonify(quiz_data_master.get_questions('APStats')) 

    class _CheckAnswer(Resource):
        def post(self):
            return quiz_data_master.check_answer(request.json['question'], request.json['answer'])
    
    class _ReadFinishQuizSummary(Resource):
        def get(self):
            return quiz_data_master.get_student_data()
            
    # building RESTapi resources/interfaces, these routes are added to Web Server
    quiz_api.add_resource(_Get, '/<string:subject>/<int:totalQsInQuiz>')
    quiz_api.add_resource(_Read, '/')
    quiz_api.add_resource(_CheckAnswer, '/checkanswer')
    quiz_api.add_resource(_ReadFinishQuizSummary, '/summary')
    
      