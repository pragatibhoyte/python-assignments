import os

def CountFileLines(FileName):

    Ret = os.path.exists(FileName)

    if Ret==False:
        print("File does not exist")

    else:

        fobj = open(FileName, "r")

        Data = fobj.read()

        Lines = Data.splitlines()

        No = 1

        for line in Lines:
            print(f"{No} : {line}")
            No+=1

        fobj.close()

def main():
    Name = input("Enter File Name: ")

    CountFileLines(Name)

if __name__ == "__main__":
    main()