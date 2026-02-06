import os
import sys

def RenamingExtensions(DirName, extension1, extension2):

    Ret = os.path.exists(DirName)

    fobj = open("Ass1.log", "w")

    if Ret==False:
        fobj.write("Directory does not exist")
        return

    if os.path.isdir(DirName) == False:
        fobj.write(f"{DirName} is not a directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for fname in FileName:
            if(fname.endswith(extension1)):

                OldPath = os.path.join(FolderName,fname)
                words = os.path.splitext(fname)
                NewName = words[0]+extension2

                NewPath = os.path.join(FolderName,NewName)

                os.rename(OldPath, NewPath)

    fobj.close()

def main():

    if len(sys.argv) != 4:
        print("Invalid Number of arguments")

    DirNm = sys.argv[1]
    extension1 = sys.argv[2]
    extension2 = sys.argv[3]

    RenamingExtensions(DirNm, extension1, extension2)

    print("Renamed file name with first extention to second extension succesfully !")

if __name__ == "__main__":
    main()