from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from tkinter import *
from tkinter import filedialog


root = Tk()
filetypes = [("PDF Files", "*.pdf")]
files = filedialog.askopenfilenames(filetypes=filetypes)
pdf_files = list(files)
save_path = filedialog.askdirectory(initialdir="C:\\", mustexist=True, title= "Where to save")
t = 0


print(pdf_files)
for pdf2 in pdf_files:
    pdf = PdfReader(pdf2)
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

            elif (k>0) & (arr[0] != "BLANK PAGE") :
                questions[k-1].add_page(p)


    k = 1 + t
    for p in questions:
        with Path(save_path+"/Question"+ str(k)+".pdf").open(mode="wb") as output_file:
            p.write(output_file)
        k += 1
        t += 1
