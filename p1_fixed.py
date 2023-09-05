from PIL import Image
import json
from fpdf import FPDF

numOfChapters = 10
maxHeight = 2260
basePath = r"D:\python_projects\teachmegcse"
questionsJson=f"{basePath}/json_files/physics_db_classified_test.json"
outputdirectory=f"{basePath}/python_files/classified/pdfs"


classifiedPdf = FPDF("portrait","pt",[1600, maxHeight])
questionNumX = 80 # is for the X coordinate for the question number
questionImageX = 160 # is for the X coordinate for the Image
currentY = 100
currentPageNumber = 1
currentQuestionNum = 1
questionData = json.load(open(questionsJson,'r'))

def getAmountOfQuestionsInChapter(chapterNum):
    amount = [x for x in questionData if x['Chapter'] == str(chapterNum)]
    return len(amount)

def getDataOfQuestionsInChapter(chapterNum):
    data = [x for x in questionData if x['Chapter'] == str(chapterNum)]
    return data

amountOfQuestions = len(questionData)


level = questionData[0]["Level"]
subject = questionData[0]["Subject"]
imagelocation=f"{basePath}/images/unsorted/{subject}/p1/"

classifiedPdf.add_page()
classifiedPdf.set_font("Arial",size=45,style="B")
for currentChapterNum in range(1, numOfChapters + 1):
    numOfQuestionsInChapter = getAmountOfQuestionsInChapter(currentChapterNum)
    questionDataInChapter = getDataOfQuestionsInChapter(currentChapterNum)

    for questionNum in range(numOfQuestionsInChapter):
        currentQuestionObject = questionDataInChapter[questionNum]
        currentImage = Image.open(f"{imagelocation}/{currentQuestionObject['questionName']}")

        if currentImage.height + currentY + 100 > maxHeight:
            classifiedPdf.add_page()
            currentY = 100
            currentPageNumber += 1

        classifiedPdf.set_xy(questionNumX, currentY)
        classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
        classifiedPdf.set_xy(questionImageX, currentY)
        classifiedPdf.image(f"{imagelocation}/{currentQuestionObject['questionName']}", questionImageX, currentY, 1420, currentImage.height)
        currentY += currentImage.height + 100
        currentQuestionNum += 1

print("complete")
classifiedPdf.output(f"{outputdirectory}/{subject}_{level}_classified.pdf")