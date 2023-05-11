from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfReader
import tkinter
from tkinter import filedialog

pdfPath = filedialog.askopenfilename(initialdir="C:\\", title= "Select Pdf")
output1Path = filedialog.askdirectory(initialdir="C:\\", mustexist=True, title= "Where to save")
images = convert_from_path(pdfPath, poppler_path= r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin')
subject = tkinter.simpledialog.askstring("Enter Subject Name", "Enter Subject Name")
currentQuestion = 1
numOfQuestionsInPage = 0
numOfQuestions = tkinter.simpledialog.askinteger("Enter Number of Questions in the past paper", "Enter Number of Questions in the past paper")
reader = PdfReader(pdfPath)

def makeImages(output1Path, pdfPath):
    images = convert_from_path(pdfPath, poppler_path= r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin')
    reader = PdfReader(pdfPath)
    numberOfPages = len(reader.pages)
    initialPage = getInitial()[0]
    for x in range(1, numberOfPages):
        images[x].save(f"{output1Path}/{x + int(initialPage)}.jpg", 'JPEG')  #Convert each page into image and save it to the directory


def getInitial():
    y = open(r"C:\Users\donat\Documents\python_projects\output1\eco\p1\numofpages.txt",'r+')
    f = open(r"C:\Users\donat\Documents\python_projects\output1\eco\p1\numofquestions.txt",'r+')
    initialQuestion = f.read()
    initialPage = y.read()
    y.close()
    f.close()
    values = [initialPage, initialQuestion]
    return values

def takeScreenshot(y1, y2, currentQuestion, i):
    initialQuestion = getInitial()[1]
    initialPage = getInitial()[0]
    with Image.open(f"{output1Path}/{i + int(initialPage)}.jpg") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            current = int(initialQuestion) + currentQuestion
            current = str(current)
            im_crop.save(f"{output1Path}/{subject}_{current}.jpg")

def numOfQuestionsInPage(currentPage, currentQuestion):
    reader = PdfReader(pdfPath)
    page = reader.pages[currentPage]
    numOfQuestionsInPage = 0
    while page.extract_text().find(f"{currentQuestion} ") != -1:
        if page.extract_text().find(f"{currentQuestion} ") != -1:
            numOfQuestionsInPage += 1
            currentQuestion += 1
    return numOfQuestionsInPage

def saveFinal(finalQuestion, finalPage):
    f = open(r"C:\Users\donat\Documents\python_projects\output1\eco\p1\numofquestions.txt",'r+')
    f.write(finalQuestion)
    f.close()
    y = open(r"C:\Users\donat\Documents\python_projects\output1\eco\p1\numofpages.txt",'r+')
    y.write(finalPage)
    y.close()

def isBlankPage(currentPage):
    reader = PdfReader(pdfPath)
    page = reader.pages[currentPage]
    if page.extract_text().find("BLANK PAGE") == -1:
        return False
    return True

def getDimensions(currentPage, prevPixel):
    im = Image.open(f"{output1Path}/{currentPage}.jpg")
    pix = im.load()
    found = False
    i = 80
    while found == False:
        if (prevPixel + i) <= 2150:
            value = pix[147,prevPixel + i]
            if value != (255, 255, 255):
                found = True
            else:
                if (prevPixel + i) >= 2150:
                    return ((prevPixel + i) - 30)
                else:
                    i += 1
        else: return ((prevPixel + i) - 30)
    return ((prevPixel + i) - 30)

initialQuestion = getInitial()[1]
initialPage = getInitial()[0]
makeImages(output1Path, pdfPath)

numberOfPages = len(reader.pages)

for i in range(1, numberOfPages):
        
    if isBlankPage(i) == True:
        continue 
    else:
        numOfQuestionsInPage1 = numOfQuestionsInPage(i, currentQuestion)
        firstQuestionInPage = True
        startY = 150
        for j in range(numOfQuestionsInPage1):
            if firstQuestionInPage:
                endY = getDimensions(i, startY)
                nextY = getDimensions(i, startY)
                takeScreenshot(startY, endY, currentQuestion, i)
                firstQuestionInPage = False
                currentQuestion += 1
            elif j == numOfQuestionsInPage1:
                startY = nextY
                endY = 2150
                takeScreenshot(startY, endY, currentQuestion, i)
                currentQuestion += 1
            else:
                startY = nextY
                endY = getDimensions(i, startY)
                nextY = getDimensions(i, startY)
                takeScreenshot(startY, endY, currentQuestion, i)
                currentQuestion += 1

finalQuestion = int(initialQuestion) + numOfQuestions
finalQuestion = str(finalQuestion) 
saveFinal(finalQuestion, finalPage= '0')