import os

code = 9702
paperNumber = 'p1'
subject = 'phy'
qnumber=1
numofQuestions = 1280
path = r"C:\Users\donat\Documents\python_projects"

print("Enter Chapter Number")
while qnumber<numofQuestions:
    if os.path.isfile(f'{path}\output\{code}\{paperNumber}\{subject}_{qnumber}.jpg')==True:
        QuestionName=f'{subject}_{qnumber}.jpg'
        chapter=input(f'{subject}_{qnumber}.jpg : ')
        os.replace(f'{path}\output\{code}\{paperNumber}'+ QuestionName,f'{path}\js_test\Classified\sorted\{code}\{paperNumber}\{chapter}\{QuestionName}')     
    qnumber+=1