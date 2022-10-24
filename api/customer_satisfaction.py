from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from customer_questions import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/customer')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class CustomerAPI:
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
            return jsonify(getQuestions(id))

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
    api.add_resource(_Create, '/create/<string:question>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateLike, '/like/<int:id>')
    api.add_resource(_UpdateNo, '/no/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'http://www.teamcheeseatimetime.tk' # run from web
    url = server + "/api/customer"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read joke by id
        ) 
    responses.append(
        requests.put(url+"/like/"+num) # add to like count
        ) 
    responses.append(
        requests.put(url+"/no/"+num) # add to jeer count
        ) 

    # obtain a random joke
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")