import os

def Searching(FileName, string):

    Ret = os.path.exists(FileName)

    if Ret==False:
        print(f"{FileName} does not exist")

    else:

        fobj = open(FileName, "r")

        Data = fobj.read()

        words = Data.split()

        isWordPresent= False

        for i in words:
            if string.lower()==i.lower():
                isWordPresent=True
                break

        if isWordPresent == True:
            print(f"{string} found in file {FileName}")
        else:
            print(f"{string} not found in file {FileName}")
            
        fobj.close()

def main():
    Filename = input("Enter file name: ")

    Name = input("Enter word to find in file: ")

    Searching(Filename, Name)

if __name__ == "__main__":
    main()