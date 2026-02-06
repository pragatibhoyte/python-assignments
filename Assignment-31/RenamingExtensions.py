import os

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
