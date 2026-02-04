import os

def CountFileLines(FileName):

    Ret = os.path.exists(FileName)

    if Ret==False:
        print("File does not exist")

    else:

        fobj = open(FileName, "r")

        Data = fobj.read()

        Lines = Data.splitlines()

        count = 0

        for line in Lines:
            count+=1

        print("Number of lines present in file : ",count)

        fobj.close()

def main():
    Name = input("Enter File Name: ")

    CountFileLines(Name)

if __name__ == "__main__":
    main()