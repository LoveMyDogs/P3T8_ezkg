import json
import os
SUBJ_STATS = "Statistics"
SUBJ_CS = "APCS"
SUBJ_Cal = "APCal"
class QuizDataMaster:
    quiz_data = []
    # Initialize questions
    def init(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "", "quiz-questions-by-subject.json")
        self.quiz_data = json.load(open(json_url))
        return self.quiz_data

    def get_questions(self, subject):
        questions = []
        return self.quiz_data[subject]

quiz_data_master  = QuizDataMaster()