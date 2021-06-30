from PyPDF2 import PdfFileMerger, PdfFileReader # pip install pypdf2

pdf_file1 = PdfFileReader("12715-notice.pdf")
pdf_file2 = PdfFileReader("12752-notice.pdf")
pdf_file3 = PdfFileReader("12756-notice.pdf")

output = PdfFileMerger()

output.append(pdf_file1)
output.append(pdf_file2)
output.append(pdf_file3)

output.write("merged.pdf")