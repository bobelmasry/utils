from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from tkinter import *
from tkinter import filedialog
from PIL import Image
import os

output1Path = r"C:\Users\donat\Documents\python_projects\output1"

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="C:\\", title= "Select file")
pdf = PdfReader(root.filename)

questions= []
k = 0
for p in pdf.pages:
        arr = p.extract_text().split('\n')
        arr.pop(0)
        arr.pop(0)
        if len(arr) > 0:
            if arr[0][0].isdigit():
                questions.append(PdfWriter())
                questions[k].add_page(p)
                k +=1
                print("question "+ str(k))

            elif (k>0) & (arr[0] != "BLANK PAGE") :
                print(k)
                questions[k-1].add_page(p)

pdfPathWithoutPDF = root.filename[:-4]
k = 1
y = 1
for p in questions:
    p.write(pdfPathWithoutPDF+"Question"+ str(k)+".pdf")
    pdfPathwithNUM = pdfPathWithoutPDF+"Question"+ str(k)+".pdf"
    images = convert_from_path(pdfPathwithNUM, poppler_path= r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin')
    reader = PdfReader(pdfPathwithNUM)
    numberOfPages = len(reader.pages)
    for x in range(numberOfPages):
        images[x].save(f"{output1Path}/eco/p1/Question{y}/{x+1}.jpg", 'JPEG')
    k += 3
    y += 1

for i in range(12):
    if os.path.isdir(f"{output1Path}/eco/p1/Question{i}"):
        lst = os.listdir(f"{output1Path}/eco/p1/Question{i}")
        print(lst)
        print(i)
        if ("0.jpg" in lst) and ("1.jpg" not in lst) and ("2.jpg" not in lst):
            img1 = Image.open(f"{output1Path}/eco/p1/Question{i}/0.jpg")
            dst = Image.new('RGB', (img1.width, img1.height))
            dst.paste(img1, (0, 0))
            dst.save(f"{output1Path}/eco/p1/1{i}.jpg")
        if ("0.jpg" in lst) and ("2.jpg" not in lst):
            img1 = Image.open(f"{output1Path}/eco/p1/Question{i}/0.jpg")    
            img2 = Image.open(f"{output1Path}/eco/p1/Question{i}/1.jpg")
            dst = Image.new('RGB', (img1.width, img1.height + img2.height))
            dst.paste(img1, (0, 0))
            dst.paste(img2, (img1.height, 0))
            dst.save(f"{output1Path}/eco/p1/2{i}.jpg")
        if ("0.jpg" in lst) and ("1.jpg" in lst) and ("2.jpg" in lst):
            img1 = Image.open(f"{output1Path}/eco/p1/Question{i}/0.jpg")
            img2 = Image.open(f"{output1Path}/eco/p1/Question{i}/1.jpg") 
            img3 = Image.open(f"{output1Path}/eco/p1/Question{i}/2.jpg")
            dst = Image.new('RGB', (img1.width, img1.height + img2.height + img3.height))
            dst.paste(img1, (0, 0))
            dst.paste(img2)
            dst.paste(img3)
            dst.save(f"{output1Path}/eco/p1/3{i}.jpg")
