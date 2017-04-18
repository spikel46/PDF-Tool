import sys, os
import PyPDF2
#import tkinter for graphics later
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader

options = ["Merge", "Invert"]

patterns = ["Append", "Alternate"]

def get_files():
    fh = ""
    filelist = list()
    while(fh != "q"):
        fh = input("Please enter a file (q to quit): ")
        #add file verification
        filelist.append(fh)
    filelist.pop()
    return filelist

def menu():
    print("Options we currently support:\n")
    for i in range(len(options)):
        print("{}: {}".format(i+1, options[i]))
    choice = int(input("Please enter your choice: "))-1
    return choice

def get_pattern():
    print("Patterns we currently support:\n")
    for i in range(len(patterns)):
        print("{}: {}".format(i+1, patterns[i]))
    pattern = int(input("Please enter your choice: "))-1
    return pattern

def merge(filelist, pattern=0):
    merger = PdfFileMerger()
    if(pattern == 0):
        for fh in filelist:
            #just put files in order
            print(fh)
            merger.append(fh)
            
    output = open("./joined.pdf","wb")
    merger.write(output)

def inv_single(fh):
    reader = PdfFileReader(fh)
    num_pages = reader.getNumPages()
    inverter = PdfFileMerger()
    print("Num Pages: {}".format(num_pages))
    inverter.append(fh, pages=(num_pages-1,-1,-1))
    output = open("./inverted.pdf","wb")
    inverter.write(output)
    
#def inverse(filelist):
    
    
def main():
    filelist = list()

    if(len(sys.argv)==1):
        filelist = get_files()
        
    if(len(sys.argv)>1):
        for fh in range(1,len(sys.argv)):
            filelist.append(sys.argv[fh])

    choice = menu()
    while(choice not in range(len(options))):
        print("Your choice was not a valid option")
        choice = menu()
    if(choice == 0):
        pattern = get_pattern()
        merge(filelist, pattern)
    if(choice == 1):
        inv_single(filelist[0])
        

main()
#if name thing here
