import os

def CopyContents(FileName1, FileName2):

    Ret1 = os.path.exists(FileName1)

    if Ret1==False:
        print(f"{FileName1} does not exist")

    else:

        fobj = open(FileName1, "r")

        Data = fobj.read()

        fobj1 = open(FileName2, "w")

        fobj1.write(Data)

        print("Data copied successfully")

        fobj.close()
        fobj1.close()

def main():
    Name1 = input("Enter Existing file name: ")

    Name2 = input("Enter new file name: ")

    CopyContents(Name1, Name2)

if __name__ == "__main__":
    main()