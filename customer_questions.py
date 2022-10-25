import random

questions_data = []


questions_list = [
    "Was the website readable?",
    "Were the explanations done well?",
    "Did you feel that the website is well decorated and exciting?",
    "Would you like an expansion to other sections or further explanations?",
    "Were our quizzes satisfactory?",
    "Are you suffering a lot in school right now?",
    "Did you feel that there were enough questions, or too many questions in the quiz?",
    "Would you have preferred a different reward for winning the quiz?",
    "If we told you customer satisfaction was our highest goal, would you have believed us?",
    'Do you think the website creators are cool?'
]

# Initialize questions
def initQuestions():
    # setup questions into a dictionary with id, question, yes, no
    item_id = 0
    for item in questions_list:
        questions_data.append({"id": item_id, "question": item, "yes": 0, "no": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomQuestion()['id']
        addQuestionYes(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomQuestion()['id']
        addQuestionNo(id)
        
# Return all questions from questions_data
def getQuestions():
    return(questions_list)

# Question getter
def getQuestion(id):
    return(questions_data[id])

# Return random question from question_data
def getRandomQuestion():
    return(random.choice(questions_data))

# Truest question
def favoriteQuestion():
    best = 0
    bestID = -1
    for question in getQuestions():
        if question['yes'] > best:
            best = question['yes']
            bestID = question['no']
    return questions_data[bestID]
    
# Jeered question,  we are doing bad lmao ;)
def worstQuestion():
    worst = 0
    worstID = -1
    for question in getQuestions():
        if question['no'] > worst:
            worst = question['no']
            worstID = question['id']
    return questions_data[worstID]

# Add to yes for requested id
def addQuestionYes(id: int):
    questions_data[id]['yes'] = questions_data[id]['yes'] + 1
    return questions_data[id]['yes']

# Add to no for requested id
def addQuestionNo(id):
    questions_data[id]['no'] = questions_data[id]['no'] + 1
    return questions_data[id]['no']

# Pretty Print question
def printQuestion(question):
    print(question['id'], question['question'], "\n", "yes:", question['yes'], "\n", "no:", question['no'], "\n")

# Number of questions
def countQuestions():
    return len(questions_data)

# Test Question Model
if __name__ == "__main__": 
    initQuestions()  # initialize questions
    
    # Most likes and most jeered
    best = favoriteQuestion()
    print("Done best", best['yes'])
    printQuestion(best)
    worst = worstQuestion()
    print("Where we did worst", worst['no'])
    printQuestion(worst)
    
    # Random question
    print("Random question")
    printQuestion(getRandomQuestion())
    
    # Count of Questions
    print("Questions Count: " + str(countQuestions()))