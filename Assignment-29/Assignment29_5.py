import os
import sys

def File(FileName, string):

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("File does not exist")
    else:
        fobj = open(FileName, "r")
        
        count = 0

        Data = fobj.read()

        Words = Data.split()

        for i in Words:
            if(i == string):
                count+=1

        print(count)
        fobj.close()

def main():

    FileName = input("Enter Filename: ")

    String =input("Enter the name you want to find :")

    File(FileName ,String )

if __name__ == "__main__":
    main()