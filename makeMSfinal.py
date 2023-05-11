import cv2 
import pytesseract
import os
import MS
import json
import re

code = 9701
paperNumber = 'p1'
subject = 'chem'
qnumber=1
path = r"C:\Users\donat\Documents\python_projects"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
custom_config = r'--oem 3 --psm 6'
index = 0
f = open(f'{subject}_mcq_answers1.json', 'w')
f.write("[")

names = ["s22_ms_11", "s22_ms_12","s22_ms_13", "s21_ms_11","s21_ms_12", "s21_ms_13", "m22_ms_12", "m21_ms_12", "w21_ms_11",
         "w21_ms_12", "w21_ms_13", "s20_ms_11", "s20_ms_12", "s20_ms_13", "m20_ms_12", "w20_ms_11", "w20_ms_12", "w20_ms_13",
         "m19_ms_12", "s19_ms_11", "s19_ms_12", "s19_ms_13", "w19_ms_11", "w19_ms_12", "w19_ms_13", "m18_ms_12", "s18_ms_11", 
        "s18_ms_12", "s18_ms_13", "w18_ms_11", "w18_ms_12", "w18_ms_13"]

while qnumber<1200:
    pdfName = names[index]
    answers = MS.getAnswers(code, pdfName)
    if qnumber % 40 == 0 and qnumber != 0:
        index += 1
        print(index)
    

    if os.path.isfile(f'{path}\output\{code}\{paperNumber}\{subject}_{qnumber}.jpg')==True:
        QuestionName=f'{subject}_{qnumber}.jpg'
        QuestionName2 = f'{subject}_{qnumber}'
        path2 = f"{path}\output\{code}\{paperNumber}\{QuestionName}"   
        img = cv2.imread(path2)
        questionText = pytesseract.image_to_string(img, config=custom_config)
        questionNumber = questionText[:2]
        questionNumber = re.sub(r'[^\w\s]', '', questionNumber)
        try:
            questionAnswer = answers[int(questionNumber) - 1]
        except:
            questionAnswer = ''
        print(f"{QuestionName}:{questionNumber}:{questionAnswer}")
        pdfName1 = f"{code}_{pdfName[:3]}_qp{pdfName[6:]}"
        if questionAnswer != '':
            answerObject = {
            "questionName" : f"{QuestionName2}",
            "Answer": f"{questionAnswer}",
            "pdfName":f"{pdfName1}"
            }
            answerObjectFormatted = json.dumps(answerObject)
            f.write(answerObjectFormatted)
            f.write(""",
""")
            
    qnumber+=1

f.write("]")
f.close()
