from PyPDF2 import PdfFileMerger

def merge_pdfs(output_path, *input_paths):
    merger = PdfFileMerger()
    for pdf in input_paths:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

# example merge_pdfs("merged.pdf", "input1.pdf", "input2.pdf")