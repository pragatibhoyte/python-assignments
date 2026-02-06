import os

def DirectoryFileSearch(DirName, extension):

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
            if(fname.endswith(extension)):
                fobj.write("File Name : "+fname+"\n")

    fobj.close()