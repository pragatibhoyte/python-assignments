import os
import sys

def File(FileName1, FileName2):

    Ret1 = os.path.exists(FileName1) 
    Ret2 = os.path.exists(FileName2)
    
    if Ret1==False:
        print(f"{FileName1} file does not exist")

    elif Ret2==False:
        print(f"{FileName2} file does not exist")

    else:
        f1 = open(FileName1, "r")
        f2 = open(FileName2, "r")

        Data1 = f1.read()

        Data2 = f2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        f1.close()
        f2.close()

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments")

    else:
        File(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()