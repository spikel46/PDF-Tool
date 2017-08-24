from PyPDF2 import PdfFileReader

reader = PdfFileReader("Teriyaki.pdf")
print("Teriyaki: {}".format(reader.getNumPages()))
reader = PdfFileReader("Yakisoba.pdf")
print("Yakisoba: {}".format(reader.getNumPages()))
