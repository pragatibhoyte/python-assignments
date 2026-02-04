import os

def main():

    file = input("Enter the name of file : ")

    Ret = os.path.exists(file)

    if Ret==True:
        print(f"{file} file exists")
    else:
        print(f"{file} file does not exist")

if __name__ == "__main__":
    main()