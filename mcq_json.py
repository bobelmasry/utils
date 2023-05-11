import json

numOfQuestions = 10
subject = 'chem'
start = 1

"""
    type answer and it automatically gets capitalized and if question not in files
    then type "pass" so we know which questions are not available
    and if done on multiple times then change the start value to the last question you left off
    and remember to remove the ] at the end of the json file before starting
"""

f = open(f'{subject}_mcq_answers.json', 'w')
f.write("[")
for i in range(start, numOfQuestions):
    answer = input(f"{subject}_{i} :").capitalize()
    answerObject = {
        "questionName" : f"{subject}_{i}",
        "Answer": f"{answer}",
        }
    answerObjectFormatted = json.dumps(answerObject)
    f.write(answerObjectFormatted)
    f.write(",")
f.write("]")
f.close()
