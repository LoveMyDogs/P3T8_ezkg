import json
import os
import random
SUBJ_Stats = "APStats"
SUBJ_Phys = "Physics"
SUBJ_Calc = "APCalc"
class QuizDataMaster:
    quiz_data = []
    current_quiz = []
    student_data = { "name" : 'na', "totalScore" : 0 }
    subject = ''
    # Initialize questions
    def init(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "", "quiz-questions-by-subject.json")
        self.quiz_data = json.load(open(json_url))
        return self.quiz_data

    def get_questions(self, subject):

        return self.quiz_data[subject]

    # Work your mom did above, work I'm doing below, trying to get new functions
    # defined in this format and failing
 
    # Here is an individual question getter, it doesn't seem to register the id
    # Probably because it's initially in json format?
    def get_question(self, subject, question):
        return self.quiz_data[subject] [question]

    #Here it's getting a random question, not sure if it works tho 
    def get_random_questions(self, subject, totalQsInQuiz:int):
        return(random.sample(self.quiz_data[subject], totalQsInQuiz))

quiz_data_master  = QuizDataMaster()