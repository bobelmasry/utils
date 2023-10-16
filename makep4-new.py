from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
import json

paperNumber = 4
subject = 'phy'
subject2 = 'physics'
level = 'A2'

start = 0

root = Tk()
filetypes = [("PDF Files", "*.pdf")]
startPage = 2 #Default is 0
startPixel = 180 # Default is 180
startYForQuestion = 20 # Default is 20
db = open(f'{subject}_db_p{paperNumber}.json', 'w')
db.write("[")

popplerPath = r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin'
numOfPagesPath = r'C:\Users\donat\Documents\python_projects\output1\eco\p1\numofpages.txt'
numberOfQuestionsPath = r'C:\Users\donat\Documents\python_projects\output1\eco\p1\numofquestions.txt'

files = filedialog.askopenfilenames(filetypes=filetypes)
pdf_files = list(files)
output1Path = r"C:\Users\donat\Documents\python_projects\js_test\Classified\makep4new\images"
heightsArr = [0 for i in range(100)]

def makeImages(output1Path, pdfPath, i):
    val = 0
    images = convert_from_path(pdfPath, poppler_path=popplerPath)
    reader = PdfReader(pdfPath)
    numberOfPages = len(reader.pages)
    initialPage = getInitial()[0]
    path = f"{output1Path}/{i}"
    if not os.path.exists(path):
                    os.makedirs(path)
    for x in range(startPage, numberOfPages):
        reader = PdfReader(pdfPath)
        page = reader.pages[x]
        if x >= startPage:
            if page.extract_text().find("BLANK PAGE") == -1:
                images[x].save(f"{output1Path}/{i}/{x + int(initialPage) - startPage + 1 - val}.jpg", 'JPEG')  #Convert each page into image and save it to the directory
            else:
                val += 1
                 


def getInitial():
    y = open(numOfPagesPath,'r+')
    f = open(numberOfQuestionsPath,'r+')
    initialQuestion = f.read()
    initialPage = y.read()
    y.close()
    f.close()
    values = [initialPage, initialQuestion]
    return values

def stripImage(imageName, folderNum):
      with PIL.Image.open(f"{output1Path}/{folderNum}/{imageName}.jpg") as im:
            im_crop = im.crop((0, startPixel, 1654, 2200))
            im_crop.save(f"{output1Path}/{folderNum}/{imageName}.jpg")

def cleanImage(imageName):
    x = 0
    im = PIL.Image.open(f"{output1Path}/questions/{imageName}")
    endYValue = im.height
    pix = im.load()
    flag = False
    if flag == False:
        for y in range(im.height - 2, 1, -2):
            for x in range(im.width - 2, 1, -2):
                value = pix[x, y]
                if value != (255, 255, 255):
                    endYValue = y + 65
                    flag = True
                    break  # Exit inner loop
            if flag:
                break  # Exit outer loop
    
    cleanedImage = im.crop((0, 0, 1500, endYValue))
    cleanedImage.save(f"{output1Path}/questions/{imageName}")

def mergeAllImages(folderNum):
    pages = os.listdir(f"{output1Path}/{folderNum}")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    height = (len(pages) - 1) * (2200 - startPixel)
    dst = PIL.Image.new('RGB', (1654, height), color='black')  # Updated color specifier
    currentHeight = 0
    for i in range(1, len(pages)):
        image_path = f"{output1Path}/{folderNum}/{pages[i]}"
        image = PIL.Image.open(image_path)
        dst.paste(image, (0, currentHeight, 1654, currentHeight + (2200 - startPixel)), mask=None)
        currentHeight += (2200 - startPixel)
    dst.save(f"{output1Path}/final/final{i}.jpg")
    heightsArr[folderNum] = currentHeight

def getDimensions(currentPage, prevPixel, stopValue):
    im = PIL.Image.open(f"{output1Path}/final/{currentPage}")
    pix = im.load()
    found = False
    i = 80
    while not found and (prevPixel + i <= stopValue):
        value = pix[147, prevPixel + i]
        if value != (255, 255, 255):
            found = True
        else:
            i += 2
    return ((prevPixel + i) - 30)


def saveFinal(finalQuestion, finalPage):
    f = open(numberOfQuestionsPath,'r+')
    f.write(finalQuestion)
    f.close()
    y = open(numOfPagesPath,'r+')
    y.write(finalPage)
    y.close()

def takeScreenshot(y1, y2, currentQuestionNum, fileName):
    if currentQuestionNum != 1 + int(initialQuestion):
        with PIL.Image.open(f"{output1Path}/final/{fileName}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            if (y2 - y1 != 50):
                im_crop.save(f"{output1Path}/questions/{subject}_{currentQuestionNum}.jpg")

            
for m in range(len(files)):
    makeImages(output1Path, files[m], m)

    questionsArray = os.listdir(output1Path)
    for i in range(len(questionsArray) - 2):
        pagesArray = os.listdir(f"{output1Path}/{questionsArray[i]}")
        currentFolder = questionsArray[i]
        for j in range(1, len(pagesArray) + 1):
            stripImage(j, currentFolder)

    for i in range(len(questionsArray) - 2):
        mergeAllImages(i)

    finalArray = os.listdir(f"{output1Path}/final")
    for i in range(len(finalArray)):
        initialQuestion = getInitial()[1]
        currentY = startYForQuestion
        currentQuestionNum = 1 + int(initialQuestion)
        stopValue = heightsArr[i] - 2
        while currentY <= stopValue:  # Add the stop condition to the loop
            endY = getDimensions(finalArray[i], currentY, stopValue)
            takeScreenshot(currentY, endY, currentQuestionNum, finalArray[i])
            currentY = endY
            currentQuestionNum += 1
        saveFinal(str(currentQuestionNum), finalPage='0')


    questionsArray = os.listdir(f"{output1Path}/questions")
    for i in range(len(questionsArray)):
        cleanImage(questionsArray[i])

    for i in range(start, len(questionsArray)):
        pdfName = files[m]
        pdfName = pdfName[-18:]
        answerObject = {
        "questionName" : questionsArray[i],
        "questionNum" : i + 1 - start,
        "Subject":subject2,
        "Level":level,
        "paperNumber":paperNumber,
        "pdfName":pdfName
        }
        answerObjectFormatted = json.dumps(answerObject)
        db.write(answerObjectFormatted)
        db.write(""",
""")
    start = len(questionsArray)

db.write("]")
db.close()

for i in range(len(os.listdir(output1Path)) - 2):
    os.remove(f"{output1Path}\\{i}")