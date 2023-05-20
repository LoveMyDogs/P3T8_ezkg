from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource , reqparse # used for REST API building
from flask import request
from quiz_questions.quiz_data_master import *
import threading  # import threading
from model.questions import *
quiz_app_api = Blueprint('quiz_api_bp', __name__,
                   url_prefix='/api/quiz')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
quiz_api = Api(quiz_app_api)

class QuizAPI:
    # not implemented
    class _Get(Resource):
        reqparse
        def get(self, subject, totalQsInQuiz:int):
            return quiz_data_master.get_random_questions(subject, totalQsInQuiz)

    class _GetByFilters(Resource):
        def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument('subject', type = str, default='',  required=False)
            self.reqparse.add_argument('sortby', type = str, default='',  required=False)
            self.reqparse.add_argument('address', type = str, default='',  required=False)
            self.reqparse.add_argument('age', type = str, default='',  required=False)
            super(QuizAPI._GetByFilters, self).__init__()

        def get(self):
            args = request.args
            #print(args)
            subject = args.get('subject')
            sortby= args.get('sortby')
            # return subject
            return 'hello' + subject + "-" + sortby
    
    class _GetAll(Resource):
            
        def get(self):
            return quiz_data_master.get_all_subjects()

    class _Read(Resource):
        def get(self):
            return jsonify(quiz_data_master.get_questions('APStats')) 

    class _CheckAnswer(Resource):
        def post(self):
            return quiz_data_master.check_answer(request.json['question'], request.json['answer'])
    
    class _ReadFinishQuizSummary(Resource):
        def get(self):
            return quiz_data_master.get_student_data()
    class _KeepUpdating(Resource):
        # build a function to run over and over
        # global variable setup
        def get(self):
            return quiz_data_master.counter()

    class _GetAllQuestions(Resource):
        def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument('subject', type = str, default='',  required=False)
            self.reqparse.add_argument('sortby', type = str, default='',  required=False)
            self.reqparse.add_argument('sorttype', type = str, default='',  required=False)
            super(QuizAPI._GetAllQuestions, self).__init__()

        def get(self):
            args = request.args
            #print(args)
            # filter by subject
            subject = args.get('subject')
            sorttype= args.get('sorttype')
            allQs = Question.query.all()
            if (sorttype == 'QSort'):
                print(sorttype)
                
            return Question.getAll()

    class _SetPinned(Resource):

        def put(self, id, isPinned):
            q = Question.getById(id)
            q.pinned = isPinned
            q.update("", "", isPinned)            
            return Question.getAll()
    

    # building RESTapi resources/interfaces, these routes are added to Web Server
    quiz_api.add_resource(_Get, '/<string:subject>/<int:totalQsInQuiz>')
    quiz_api.add_resource(_Read, '/')
    quiz_api.add_resource(_CheckAnswer, '/checkanswer')
    quiz_api.add_resource(_ReadFinishQuizSummary, '/summary')
    quiz_api.add_resource(_KeepUpdating, '/counter')
    quiz_api.add_resource(_GetByFilters, '/filters')
    quiz_api.add_resource(_GetAll, '/subjects')
    
    quiz_api.add_resource(_GetAllQuestions, '/questions')
    quiz_api.add_resource(_SetPinned, '/questions/pin/<int:id>/<int:isPinned>')