import json
import os
import cv2 
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
custom_config = r'--oem 3 --psm 6'
path = r"C:\Users\donat\Documents\python_projects\js_test\Classified\sorted\9701\sortedp1"

numOfQuestions = 1255
numOfChapters = 22
subject = 'chem'
level = 'AS'
code = 9701
paperNumber = 1
f = open(f'{subject}_mcq_answers1.json', 'r')
db = open(f'{subject}_db1.json', 'w')
data = json.load(f)
db.write("[")

for chapter in range(1, numOfChapters):
    directory = f"C:/Users/donat/Documents/python_projects/js_test/Classified/sorted/{code}/sortedp1/{chapter}"
    lst = os.listdir(directory) # your directory path
    number_files = len(lst)
    print(number_files)
    for i in range(1, numOfQuestions):
        if os.path.isfile(f"C:\\Users\\donat\\Documents\\python_projects\\js_test\\Classified\\sorted\\{code}\\sortedp1\\{chapter}\\{subject}_{i}.jpg") == True:
                print(f'C:/Users/donat/Documents/python_projects/js_test/Classified/sorted/{code}/sortedp1/{chapter}/{subject}_{i}.jpg')
                questionName= subject + "_" + str(i)
                img = cv2.imread(f'{path}\{chapter}\{questionName}.jpg')
                questionText = pytesseract.image_to_string(img, config=custom_config)
                questionText = re.sub(r'[^\w\s]', '', questionText)
                questionText = re.sub(r'\d+', '', questionText)
                questionText = questionText.lower()
                for question in data:
                    if question["questionName"] == questionName:
                        Answer = question["Answer"]
                        pdfName = question["pdfName"]
                        answerObject = {
                            "questionName" : f"{subject}_{i}.jpg",
                            "Answer": f"{Answer}",
                            "Chapter":chapter,
                            "Subject":subject,
                            "Level":level,
                            "paperNumber":paperNumber,
                            "questionText":questionText,
                            "pdfName":f"{pdfName}"
                        }
                        answerObjectFormatted = json.dumps(answerObject)
                        db.write(answerObjectFormatted)
                        db.write(""",
""")
        else:
             i +=1

f.close()
db.write("]")
db.close()