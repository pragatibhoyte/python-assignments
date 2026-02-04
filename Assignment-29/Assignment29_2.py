import os

def main():

    file = input("Enter the name of file : ")

    Ret = os.path.exists(file)

    if Ret==True:
        print(f"{file} file exists")

        fobj = open(file, "r")

        Data = fobj.read()

        print(f"Contents of File {file} are : ", Data)
        fobj.close()


    else:
        print(f"{file} file does not exists")

if __name__ == "__main__":
    main()