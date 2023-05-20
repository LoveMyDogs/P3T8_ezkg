import json
import os
import random
import threading
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

    def get_all_questions(self):
        subjects = []
        for subject in self.quiz_data:           
            for q in self.quiz_data[subject]:
                # print(q["id"])
                subjects.append ( { 
                    "subject": subject, 
                    "id" : q["id"], 
                    "question": q['question'],
                    "answer": q['answer'],
                    "pinned": False})
        return subjects

    
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
    _counter = 0
    def keepUpdating(self): # build a function to run over and over  
        # global variable setup
        global run_counter
        try: run_counter
        except: run_counter = 0
        # print("Seconds:", run_counter)  # replace this line with updates to data
        self._counter = run_counter
        run_counter += 3  # this is update to global variable
        threading.Timer(1.0, self.keepUpdating).start()
    
    def counter(self):
        return self._counter

    
    def bubbleSort(self, list):
        n = len(list) - 1  # list are indexed 0 to n-1, len is n
        # Traverse through list with i index

        for i in range(n):

            swapped = False  # optimize code, so it exits if now swaps on inner loop
            # Inner traversal using j index
            for j in range(n-i):  # n-i as positions on right are in order in bubble

                # Swap if the element KeyN is greater KeyN1
                keyN = list[j]
                keyN1 = list[j+1]
                if keyN > keyN1:
                    swapped = True
                    list[j], list[j + 1] = list[j + 1], list[j]  # single line swap

            if not swapped:  # if no swaps on inner pass, list is sorted
                return  # exit function    
    def selectionSort(self, list):
        n = len(list)  # length is n
        # List is traversed from index 0 to n-1, n elements
        for i in range(n):
            smallI = i  # small index is captured
            smallV = list[i]
            # Inner traversal looks at elements after i

            for j in range(i+1, n):
                # Save reference if less
                keyV = list[j]
                if keyV < smallV:
                    smallI = j  # small index is replaced
                    smallV = keyV

            # swap smallest to current i positon, sorting left to right

            list[i], list[smallI] = list[smallI], list[i]  # single line swap

     # bubble sorts a list of dictionaries, base off of provided key

    def bubbleSort(self, list, key):
        n = len(list) - 1  # list are indexed 0 to n-1, len is n
        # Traverse through list with i index
        for i in range(n):
            swapped = False  # optimize code, so it exits if now swaps on inner loop
            # Inner traversal using j index

            for j in range(n-i):  # n-i as positions on right are in order in bubble
                # Swap if the element KeyN is greater KeyN1
                keyN = list[j].get(key)
                keyN1 = list[j+1].get(key)
                if keyN > keyN1:
                    swapped = True
                    list[j], list[j + 1] = list[j + 1], list[j]  # single line swap

            if not swapped:  # if no swaps on inner pass, list is sorted
                return  # exit function

    def Save(self, questions, subjects):
        for q in questions:
            subj = q["subject"]
            print(q)
            for s in subjects:
                if (subj in s):
                    data = s[subj]
                    if data["id"] == q["id"]:
                        data["desc"] = q["desc"]
                        print ('xxx')
                    print(s)
                    
quiz_data_master  = QuizDataMaster()