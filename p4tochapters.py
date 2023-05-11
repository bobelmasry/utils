import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from PyPDF2 import PdfReader

code = 9618
paperNumber = 'p3'
qnumber=1
numofQuestions = 1280
path = r"C:\Users\donat\Documents\python_projects"

def getPdfText(pdfPath):
    reader = PdfReader(pdfPath)
    numOfPages = len(reader.pages)
    text = ''
    for i in range(numOfPages):
        page = reader.pages[i]
        parts = []
        def visitor_body(text, cm, tm, fontDict, fontSize):
            y = tm[5]
            if y > 40 and y < 720:
                parts.append(text)

        page.extract_text(visitor_text=visitor_body)
        text_body = "".join(parts)
        text += text_body
    return text



def makeText(pdfPath):
        text = getPdfText(pdfPath)
        stop_words = set(stopwords.words('english'))

        # Convert all text to lowercase
        text = text.lower()

        # Remove punctuation, digits, and non-alphabetic characters
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        

        # Tokenize text into words
        words = word_tokenize(text)

        # Remove stop words
        words = [w for w in words if w not in stop_words]

        # Join the processed words back into a single string
        return ' '.join(words)


print("Enter Chapter Number")
while qnumber<numofQuestions:
    if os.path.isfile(f'{path}\output\{code}\{paperNumber}\Question{qnumber}.pdf')==True:
        print(makeText(f'{path}\output\{code}\{paperNumber}\Question{qnumber}.pdf'))
        QuestionName=f'Question{qnumber}.pdf'
        chapter=input(f'Question{qnumber}.pdf : ')
        os.replace(f'{path}\output\{code}\{paperNumber}\{QuestionName}',f'{path}\js_test\Classified\sorted\{code}\{paperNumber}\{chapter}\{QuestionName}')     
    qnumber+=1