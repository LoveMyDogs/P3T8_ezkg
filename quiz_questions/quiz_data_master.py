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

    def check_answer(self, questId, answer):
        QnA = {}
        result = {
            'correctAnswer': '', 
            'scoreForThisAnswer': 0,
            'totalScore': 0, 
            'solution': ''
        }
        # Todo: question->id 
        for q in self.current_quiz:
            if questId == q['id']:
                QnA = q
                break
        
        if (QnA == {}):
            return 'Cannot find question'

        result['correctAnswer'] =  QnA['answer']
        result['solution'] =  QnA['solution']
        if (answer == QnA['answer']):
            self.student_data['totalScore'] =  self.student_data['totalScore'] + QnA['score']
            result['scoreForThisAnswer'] = QnA['score']
            print('Good answer for : ', QnA['question'], QnA['score'])
        else:
            # no score since answer is incorrect. 
            # UI can check for this value and display incorrect message
            # and with correct answer
            result['scoreForThisAnswer'] = 0

        result['totalScore'] = self.student_data['totalScore']
        return result
        
quiz_data_master  = QuizDataMaster()