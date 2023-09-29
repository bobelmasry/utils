from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image
from fpdf import FPDF
import tempfile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    Level: str
    Answer: str
    Chapter: str
    Subject: str
    pdfName: str
    paperNumber: int
    questionName: str
    questionText: str

class QuestionsList(BaseModel):
    questionData: List[Question]

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate-pdf/")
async def generate_pdf(questionData: QuestionsList):
    questionData = questionData.questionData
    maxHeight = 2260
    basePath = r"D:\python_projects\teachmegcse"
    outputdirectory=f"{basePath}/python_files/classified/pdfs"

    classifiedPdf = FPDF("portrait","pt",[1600, maxHeight])
    questionNumX = 80  # is for the X coordinate for the question number
    questionImageX = 160  # is for the X coordinate for the Image
    currentY = 100
    currentQuestionNum = 1

    subject = questionData[0].Subject
    imagelocation=f"{basePath}/images/unsorted/{subject}/p1/"
    numOfChapters = len([x for x in questionData if x.Subject == subject])

    classifiedPdf.add_page()
    classifiedPdf.set_font("helvetica",size=45,style="B")
    for currentChapterNum in range(1, numOfChapters + 1):
        numOfQuestionsInChapter = len([x for x in questionData if x.Chapter == str(currentChapterNum)])
        questionDataInChapter = [x for x in questionData if x.Chapter == str(currentChapterNum)]

        for questionNum in range(numOfQuestionsInChapter):
            currentQuestionObject = questionDataInChapter[questionNum]
            currentImage = Image.open(f"{imagelocation}/{currentQuestionObject.questionName}")
            currentImageCropped = currentImage.crop((0, 0, currentImage.width, currentImage.height - 10))

            if currentImage.height + currentY + 100 > maxHeight:
                classifiedPdf.add_page()
                currentY = 100
                classifiedPdf.set_xy(800, -2200)
                classifiedPdf.cell(0, 10, str(classifiedPdf.page_no()), 'C')

            classifiedPdf.set_xy(questionNumX, currentY)
            classifiedPdf.cell(w=10, txt=f"{currentQuestionNum})")
            classifiedPdf.set_xy(questionImageX, currentY)
            temp_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            currentImageCropped.save(temp_image_path.name, format="JPEG")

            # Add the image to the PDF from the temporary file
            classifiedPdf.image(temp_image_path.name, questionImageX, currentY, 1420, currentImageCropped.height)
            currentY += currentImageCropped.height + 100
            currentQuestionNum += 1

    classifiedPdf.output(f"{outputdirectory}/1.pdf")

    # Return the PDF for download
    return FileResponse(f"{outputdirectory}/1.pdf")