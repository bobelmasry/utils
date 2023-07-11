from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os

paperNumber = 4
subject = 'phy'
subject2 = 'physics'
level = 'A2'

current_question_num = 0

root = Tk()
filetypes = [("PDF Files", "*.pdf")]
startPage = 2  # Default is 0
startPixel = 180  # Default is 180

popplerPath = r'C:\Users\donat\Documents\python_projects\js_test\poppler-22.12.0\Library\bin'

files = filedialog.askopenfilenames(filetypes=filetypes)
pdf_files = list(files)
output1Path = r"C:\Users\donat\Documents\python_projects\js_test\Classified\makep4new\images"
heightsArr = [0 for _ in range(100)]


def makeImages(output_path, pdf_path, i):
    images = convert_from_path(pdf_path, poppler_path=popplerPath)
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    path = f"{output_path}/{i}"
    if not os.path.exists(path):
        os.makedirs(path)
    for x in range(startPage, number_of_pages):
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
        cleaned_image = im.crop((0, 0, 1500, y))
        cleaned_image.save(f"{output1Path}/questions/{questions[i]}")


def merge_all_images(folder_num):
    pages = os.listdir(f"{output1Path}/{folder_num}")
    pages = sorted(pages, key=lambda x: int(x.split(".")[0]))
    height = (len(pages) - 1) * (2200 - startPixel)
    dst = PIL.Image.new('RGB', (1654, height), color='black')
    current_height = 0
    for i in range(1, len(pages)):
        image_path = f"{output1Path}/{folder_num}/{pages[i]}"
        image = PIL.Image.open(image_path)
        dst.paste(image, (0, current_height, 1654, current_height + (2200 - startPixel)), mask=None)
        current_height += (2200 - startPixel)
    dst.save(f"{output1Path}/final/final{folder_num}.jpg")
    heightsArr[folder_num] = current_height


def get_dimensions(current_page, prev_pixel, stop_value):
    im = PIL.Image.open(f"{output1Path}/final/{current_page}")
    pix = im.load()
    found = False
    i = 80
    while not found and (prev_pixel + i <= stop_value):
        value = pix[147, prev_pixel + i]
        if value != (255, 255, 255):
            found = True
        else:
            i += 2
    return (prev_pixel + i) - 30


def take_screenshot(y1, y2, current_question_num, file_name):
    if (y2 - y1) > 300 :
        with PIL.Image.open(f"{output1Path}/final/{file_name}") as im:
            im_crop = im.crop((100, y1, 1600, y2))
            im_crop.save(f"{output1Path}/questions/{subject}_{current_question_num}.jpg")


for m in range(len(files)):
    makeImages(output1Path, files[m], m)

    strip_images(m)
    merge_all_images(m)

    current_y = 0
    stop_value = heightsArr[m] - 2
    while current_y <= stop_value:
        end_y = get_dimensions(f"final{m}.jpg", current_y, stop_value)
        take_screenshot(current_y, end_y, current_question_num, f"final{m}.jpg")
        current_y = end_y
        current_question_num += 1

    questions_array = os.listdir(f"{output1Path}/questions")
    clean_images()