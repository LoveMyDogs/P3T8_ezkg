from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource , reqparse # used for REST API building
from flask import request

from customer_questions import *

import threading  # import threading
from model.questions import *
customers_app_api = Blueprint('customers_api_bp', __name__,
                   url_prefix='/api/customers')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
customers_api = Api(customers_app_api)


class CustomersAPI:
    # not implemented
    class _Create(Resource):
        def post(self, question):
            pass
            
       # getQuestions()
    class _Read(Resource):
        def get(self):
            return jsonify(getQuestions())

    # getQuestion(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getQuestion(id))

    # getRandomQuestion()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomQuestion())
    
    # getRandomQuestion()
    class _ReadCount(Resource):
        def get(self):
            count = countQuestions()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addQuestionYes
    class _UpdateLike(Resource):
        def put(self, id):
            addQuestionYes(id)
            return jsonify(getQuestion(id))

    # put method: addQuestionNo
    class _UpdateNo(Resource):
        def put(self, id):
            addQuestionNo(id)
            return jsonify(getQuestion(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    customers_api.add_resource(_Create, '/create/<string:question>')
    customers_api.add_resource(_Read, '/all')
    customers_api.add_resource(_ReadID, '/<int:id>')
    customers_api.add_resource(_ReadRandom, '/random')
    customers_api.add_resource(_ReadCount, '/count')
    customers_api.add_resource(_UpdateLike, '/like/<int:id>')
    customers_api.add_resource(_UpdateNo, '/no/<int:id>')