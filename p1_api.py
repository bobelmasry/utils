from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
from PIL import Image
from fpdf import FPDF
import json

app = FastAPI()

@app.post("/generate-pdf/")
async def generate_pdf(questionData):
    questionData = json.loads(questionData)
    maxHeight = 2260
    basePath = r"D:\python_projects\teachmegcse"
    outputdirectory=f"{basePath}/python_files/classified/pdfs"


    classifiedPdf = FPDF("portrait","pt",[1600, maxHeight])
    questionNumX = 80 # is for the X coordinate for the question number
    questionImageX = 160 # is for the X coordinate for the Image
    currentY = 100
    currentPageNumber = 1
    currentQuestionNum = 1

    level = questionData[0]["Level"]
    subject = questionData[0]["Subject"]
    imagelocation=f"{basePath}/images/unsorted/{subject}/p1/"
    numOfChapters = len([x for x in questionData if x['Subject'] == str(subject)])

    classifiedPdf.add_page()
    classifiedPdf.set_font("helvetica",size=45,style="B")
    for currentChapterNum in range(1, numOfChapters + 1):
        numOfQuestionsInChapter = len([x for x in questionData if x['Chapter'] == str(currentChapterNum)])
        questionDataInChapter = [x for x in questionData if x['Chapter'] == str(currentChapterNum)]

        for questionNum in range(numOfQuestionsInChapter):
            currentQuestionObject = questionDataInChapter[questionNum]
            currentImage = Image.open(f"{imagelocation}/{currentQuestionObject['questionName']}")

            if currentImage.height + currentY + 100 > maxHeight:
                classifiedPdf.add_page()
                currentY = 100
                currentPageNumber += 1
                classifiedPdf.set_xy(800, -2200)
                classifiedPdf.cell(0, 10, str(classifiedPdf.page_no()), 'C')

            classifiedPdf.set_xy(questionNumX, currentY)
            classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
            classifiedPdf.set_xy(questionImageX, currentY)
            classifiedPdf.image(f"{imagelocation}/{currentQuestionObject['questionName']}", questionImageX, currentY, 1420, currentImage.height)
            currentY += currentImage.height + 100
            currentQuestionNum += 1

    classifiedPdf.output(f"{outputdirectory}/1.pdf")

    # Return the PDF for download
    return FileResponse(f"{outputdirectory}/1.pdf")