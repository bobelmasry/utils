from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os

subject = 'eco'

current_question_num = 0

root = Tk()
filetypes = [("PDF Files", "*.pdf")]
startPage = 1  # Default is 1
startPixel = 150  # Default is 150

files = filedialog.askopenfilenames(filetypes=filetypes)
output1Path = r"D:\python_projects\teachmegcse\python_files\makep1\testImages"


def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=r"D:\python_projects\poppler-23.05.0\Library\bin")
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    for x in range(number_of_pages):
        reader = PdfReader(pdf_path)
        page = reader.pages[x]
        if x >= startPage:
            if page.extract_text().find("BLANK PAGE") == -1:
                images[x].save(f"{output_path}/{i}/{x}.jpg", 'JPEG')


def strip_images(folder_num):
    pages = os.listdir(f"{output1Path}/{folder_num}")
    for i in range(len(pages)):
        with PIL.Image.open(f"{output1Path}/{folder_num}/{pages[i]}") as im:
            im_crop = im.crop((0, startPixel, 1654, 2200))
            im_crop.save(f"{output1Path}/{folder_num}/{pages[i]}")


def clean_images():
    questions = os.listdir(f"{output1Path}/questions")
    for i in range(len(questions)):
        im = PIL.Image.open(f"{output1Path}/questions/{questions[i]}")
        pix = im.load()
        flag = False
        if flag == False:
            for y in range(im.height - 2, 1, -2):
                for x in range(im.width - 2, 1, -2):
                    value = pix[x, y]
                    if value != (255, 255, 255):
                        flag = True
                        break
                if flag:
                    break
        cleaned_image = im.crop((0, 0, 1500, y + 10))
        cleaned_image.save(f"{output1Path}/questions/{questions[i]}")


def get_dimensions(current_page, prev_pixel, folderNum):
    im = PIL.Image.open(f"{output1Path}/{folderNum}/{current_page}")
    pix = im.load()
    found = False
    i = 80
    while not found and (prev_pixel + i <= 2010):
        value = pix[147, prev_pixel + i]
        if value != (255, 255, 255):
            found = True
        else:
            i += 2
    return (prev_pixel + i)


def take_screenshot(y1, y2, current_question_num, file_name, folderNum):
    if (y2 - y1) > 100 :
        with PIL.Image.open(f"{output1Path}/{folderNum}/{file_name}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output1Path}/questions/{subject}_{current_question_num}.jpg")


for m in range(len(files)):
    makeImages(output1Path, files[m], m)

    strip_images(m)
    pages = os.listdir(f"{output1Path}/{m}")
    sorted_files = sorted(pages, key=lambda x: int(x.split('.')[0]))
    for k in range(len(pages)):
        current_y = 0
        while current_y <= 2020:
            end_y = get_dimensions(sorted_files[k], current_y, m)
            take_screenshot(current_y, end_y, current_question_num,sorted_files[k], m)
            current_y = end_y
            current_question_num += 1
            
clean_images()