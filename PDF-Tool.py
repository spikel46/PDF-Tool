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

def merge(filelist, out_name, pattern=0):
    merger = PdfFileMerger()
    if(pattern == 0):
        for fh in filelist:
            #just put files in order
            print("Adding {}...".format(fh))
            merger.append(fh)
    if(pattern == 1):
        count = 0
        num_pages = 0
        files = []
        for fh in filelist:
            reader = PdfFileReader(fh)
            pages = reader.getNumPages()
            files.append({fh:pages})
            num_pages+=pages
            
        while(count < num_pages):
            fh = list(files[count%len(filelist)].keys())[0]
            files[count%len(filelist)][fh] -= 1
            print(count,files[count%len(filelist)])
            count+=1
            
    output = open("./{}.pdf".format(out_name),"wb")
    merger.write(output)

def inv_single(fh, out_name, count):
    reader = PdfFileReader(fh)
    num_pages = reader.getNumPages()
    inverter = PdfFileMerger()
    print("Num Pages: {}".format(num_pages))
    inverter.append(fh, pages=(num_pages-1,-1,-1))
    output = open("./{}-{}".format(out_name, count),"wb")
    inverter.write(output)
    
def inverse(filelist,out_name):
    count = 1
    for fh in filelist:
        inv_single(fh, out_name, count)
        count +=1
    
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

    file_name = input("Desired output file name (without .pdf): ")
        
    if(choice == 0):
        pattern = get_pattern()
        merge(filelist, file_name, pattern)
    if(choice == 1):
        inverse(filelist, file_name)
        
if __name__ == "__main__":
    main()
