from PyPDF2 import PdfReader
pdfPath = r"C:\Users\donat\Documents\python_projects\Teachmegcse\teachmegcse3\Teachmegcse1\static\past_papers\9708\9708_s18_ms_12.pdf"

def numOfQuestionsInPage(currentPage, currentQuestion):
    reader = PdfReader(pdfPath)
    page = reader.pages[currentPage]
    numOfQuestionsInPage = 0
    while page.extract_text().find(f"{currentQuestion} ") != -1:
        if page.extract_text().find(f"{currentQuestion} ") != -1:
            numOfQuestionsInPage += 1
            currentQuestion += 1
    return numOfQuestionsInPage

currentPage = 1
numOfQuestions = 40
answers = []
answer2 = []

reader = PdfReader(pdfPath)
page = reader.pages[currentPage]
for i in range(2):
    page = reader.pages[i+1]
    pageText = page.extract_text()
    if i == 0:
            Question = 1
            start = 120
    elif i == 1:
            Question = 29
            start = 120
    for j in range(1, numOfQuestionsInPage(i+1,Question) + 1):
                if i ==1:
                      j = j+28

                index = pageText.find(f"{j} ", start)
                if j >= 10:
                      value = pageText[index:index+4]
                      answers += value
                else:
                      value = pageText[index:index+3]
                      answers += value

for j in range(len(answers)):
      if answers[j] == "A" or answers[j] =="B" or answers[j] =="C" or answers[j] =="D":
            answer2 += answers[j]
print(answer2)
print(len(answer2))


