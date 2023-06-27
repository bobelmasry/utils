from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog, simpledialog
import os

root = Tk()
filetypes = [("PDF Files", "*.pdf")]

startPage = 1 #Default is 1, 3 for phy AS
popplerPath = r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin'
initialPage = 0
initialQuestion = 0


files = filedialog.askopenfilenames(filetypes=filetypes)
pdf_files = list(files)
output1Path = filedialog.askdirectory(initialdir="C:\\", mustexist=True, title= "Where to save")
subject = simpledialog.askstring("Enter Subject Name", "Enter Subject Name")
numOfQuestions = simpledialog.askinteger("Enter Number of Questions in the past paper", "Enter Number of Questions in the past paper")


def makeImages(output1Path, pdfPath):
    images = convert_from_path(pdfPath, poppler_path=popplerPath)
    reader = PdfReader(pdfPath)
    numberOfPages = len(reader.pages)
    for x in range(1, numberOfPages):
        images[x].save(f"{output1Path}/{x + int(initialPage)}.jpg", 'JPEG')  #Convert each page into image and save it to the directory


def takeScreenshot(y1, y2, currentQuestion, i):
    with PIL.Image.open(f"{output1Path}/{i + int(initialPage)}.jpg") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            current = int(initialQuestion) + currentQuestion
            current = str(current)
            im_crop.save(f"{output1Path}/{subject}_{current}.jpg")

def numOfQuestionsInPage(currentPage, currentQuestion):
    reader = PdfReader(pdfPath)
    page = reader.pages[currentPage]
    numOfQuestionsInPage2 = 0
    while page.extract_text().find(f"{currentQuestion} ") != -1:
        if page.extract_text().find(f"{currentQuestion} ") != -1:
            numOfQuestionsInPage2 += 1
            currentQuestion += 1
    return numOfQuestionsInPage2

def isBlankPage(currentPage):
    reader = PdfReader(pdfPath)
    page = reader.pages[currentPage]
    if page.extract_text().find("BLANK PAGE") == -1:
        return False
    return True

def getDimensions(currentPage, prevPixel):
    im = PIL.Image.open(f"{output1Path}/{currentPage}.jpg")
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


for pdfPath in pdf_files:
    currentQuestion = 1
    numOfQuestionsInPage1 = 0
    reader = PdfReader(pdfPath)
    makeImages(output1Path, pdfPath)

    numberOfPages = len(reader.pages)

    for i in range(startPage, numberOfPages):
            
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
                    if (endY - startY) == 50:
                        endY = endY + 15
                    takeScreenshot(startY, endY, currentQuestion, i)
                    firstQuestionInPage = False
                    if (endY - startY) != 65:
                        currentQuestion += 1
                elif j == numOfQuestionsInPage1:
                    startY = nextY
                    endY = 2150
                    if (endY - startY) == 50:
                        endY = endY + 15
                    takeScreenshot(startY, endY, currentQuestion, i)
                    if (endY - startY) != 65:
                        currentQuestion += 1
                else:
                    startY = nextY
                    endY = getDimensions(i, startY)
                    nextY = getDimensions(i, startY)
                    if (endY - startY) == 50:
                        endY = endY + 15
                    takeScreenshot(startY, endY, currentQuestion, i)
                    if (endY - startY) != 65:
                        currentQuestion += 1

    initialQuestion += numOfQuestions

    lst = os.listdir(output1Path) # your directory path

def cleanImage(imageName):
    x = 0
    im = PIL.Image.open(f"{output1Path}/{imageName}")
    endYValue = im.height
    pix = im.load()
    flag = False
    if flag == False:
        for y in range(im.height - 2, 1, -2):
            for x in range(im.width - 2, 1, -2):
                value = pix[x, y]
                if value != (255, 255, 255):
                    endYValue = y + 45
                    flag = True
                    break  # Exit inner loop
            if flag:
                break  # Exit outer loop
    
    cleanedImage = im.crop((0, 0, 1500, endYValue ))
    cleanedImage.save(f"{output1Path}/{imageName}")


for k in range(len(lst)):
    cleanImage(lst[k])