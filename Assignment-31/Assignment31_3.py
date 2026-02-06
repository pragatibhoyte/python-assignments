import os
import sys

def CopyFiles(DirName1, DirName2):

    Ret1 = os.path.exists(DirName1)
    Ret2 = os.path.exists(DirName2)

    if(Ret1 == False):
        print(f"{DirName1} does not exist")

    if( os.path.isdir(DirName1) == False):
        print(f"{DirName1} is not a directory")
        return 

    if(Ret1 == True and Ret2 == True):
        print(f"{DirName2} already exist")
        return 
    
    os.mkdir(DirName2)
    print(f"{DirName2} created successfuly")
    
    for FolderName, SubFolderName, FileName in os.walk(DirName1):

        for fname in FileName:
            dirpath1 = os.path.join(FolderName, fname)
            dirpath2 = os.path.join(DirName2, fname)

            obj1 = open(dirpath1, "r")
            Data = obj1.read()

            obj2 = open(dirpath2, "w")
            obj2.write(Data)

    obj1.close()
    obj2.close()

def main():

    if len(sys.argv) != 3:
        print("Invalid Number of arguments")

    DirNm1 = sys.argv[1]
    DirNm2 = sys.argv[2]

    CopyFiles(DirNm1, DirNm2)

    print("Copied File contents successfullyy !")

if __name__ == "__main__":
    main()