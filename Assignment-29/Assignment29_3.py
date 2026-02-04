import os
import sys

def File(FileName):

    Ret = os.path.exists(FileName)
    
    if Ret==False:
        print("This file does not exist")
    else:
        f2 = open(FileName, "r")

        Data = f2.read()

        fobj = open("Demo.txt", "w")

        fobj.write(Data)

        print("Data Copied Successfully")

        fobj.close()
        f2.close()

def main():

    if len(sys.argv) != 2:
        print("Invalid number of argumnets")

    else:
        File(sys.argv[1])

if __name__ == "__main__":
    main()