from PyPDF2 import PdfFileMerger

filelist = ["Yakisoba.pdf","Teriyaki.pdf"]
merger = PdfFileMerger()
for fh in filelist:
    #just put files in order
    print(fh)
    merger.append(fh)
        
output = open("./joined.pdf","wb")
merger.write(output)

"""
merger = PdfFileMerger()
merger.append("Yakisoba.pdf")
merger.append("Teriyaki.pdf")
output = open("./joined.pdf","wb")
merger.write(output)
"""
