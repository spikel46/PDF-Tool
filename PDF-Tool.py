import sys, os
import pypdf2

def merge(filelist, pattern=0):
    if(pattern == 0):
        for fh in filelist:
            #just put files in order
            print(fh)

def main():
    filelist=[]
    if(len(sys.argv)>1):
        for fh in range(2,len(sys.argv)):
            filelist.append(i)
    merge(filelist)
main()
#if name thing here
