import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger

class PDFMergerApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF Merger")

        self.pdf_files = []

        self.select_button = tk.Button(master, text="Select PDFs", command=self.select_pdfs)
        self.select_button.pack()

        self.merge_button = tk.Button(master, text="Merge PDFs", command=self.merge_pdfs, state=tk.DISABLED)
        self.merge_button.pack()

    def select_pdfs(self):
        filetypes = [("PDF Files", "*.pdf")]
        files = filedialog.askopenfilenames(filetypes=filetypes)
        self.pdf_files = list(files)
        if self.pdf_files:
            self.merge_button.config(state=tk.NORMAL)

    def merge_pdfs(self):
        merger = PdfFileMerger()
        for pdf in self.pdf_files:
            merger.append(pdf)
        output_filename = filedialog.asksaveasfilename(defaultextension=".pdf")
        merger.write(output_filename)
        merger.close()

root = tk.Tk()
app = PDFMergerApp(root)
root.mainloop()
