import os

def CountFileWords(FileName):

    Ret = os.path.exists(FileName)

    if Ret==False:
        print("File does not exist")

    else:

        fobj = open(FileName, "r")

        Data = fobj.read()

        words = Data.split()

        count = 0

        for word in words:
            count+=1

        print("Number of words present in file : ",count)

        fobj.close()

def main():
    Name = input("Enter File Name: ")

    CountFileWords(Name)

if __name__ == "__main__":
    main()