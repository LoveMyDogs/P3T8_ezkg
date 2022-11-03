import json
import os
import random
SUBJ_Stats = "APStats"
SUBJ_Phys = "Physics"
SUBJ_Calc = "APCalc"
class QuizDataMaster:
    quiz_data = []
    student_data = {
            'correctAnswer': '', 
            'yourAnswer': '', 
            'scoreForThisAnswer': 0,
            'totalScore': 0, 
            'solution': '',
            'totalCorrectAnswers':0,
            'totalWrongAnswers':0,
            'percentage':0
    }
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
        self.subject = subject
        quiz = random.sample(self.quiz_data[subject], totalQsInQuiz)
        print('Create quiz with questions:')
        print(quiz)
        print('---------------------------------------------------------------------------------\n\n')  
        return quiz

    def check_answer(self, questId, answer):
        QnA = {}
              
        for q in self.quiz_data[self.subject]:           
            if questId == q['id']:
                QnA = q
                break

        print('\n\n---------------------------------------------------------------------------------')  
        print('Found question:', QnA)

        if (len(QnA) == 0):
            return f'Cannot find question {questId} in quiz'

        self.student_data['yourAnswer'] =  answer
        self.student_data['correctAnswer'] =  QnA['answer']
        self.student_data['solution'] =  QnA['solution']
        if (answer == QnA['answer']):
            self.student_data['totalScore'] =  self.student_data['totalScore'] + QnA['score']
            self.student_data['scoreForThisAnswer'] = QnA['score']          
            self.student_data['totalCorrectAnswers'] =  self.student_data['totalCorrectAnswers']  + 1
        else:
            # no score since answer is incorrect. 
            # UI can check for this value and display incorrect message
            # and with correct answer
            self.student_data['scoreForThisAnswer'] = 0
            self.student_data['totalWrongAnswers'] =  self.student_data['totalWrongAnswers'] 

        self.student_data['totalScore'] = self.student_data['totalScore']

        print('Answer result:', self.student_data)
        print('---------------------------------------------------------------------------------\n\n')  
        return self.student_data

    def get_student_data(self):
        return {
            "totalScores":  self.student_data['totalScore'] ,
            "totalCorrectAnswers":  self.student_data['totalCorrectAnswers'] ,
            "totalWrongAnswers":  self.student_data['totalWrongAnswers'] ,
            "percentage":  self.student_data['percentage'] 
            }
        
quiz_data_master  = QuizDataMaster()