import hashlib
import os
import sys

def FileChecksum(FileName):

    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024) # 1kb = 1024 bytes

    while( len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DisplayDuplicate(Directory):

    fobj = open("log.txt","w")

    if(os.path.exists(Directory) == False):
        fobj.write(f"{Directory} directory does not exist")
        return

    if(os.path.isdir(Directory) == False):
        fobj.write(f"{Directory} is not directory")
        return
    
    Duplicate = {}
    for FolderName, SubFolderName, FileName in os.walk(Directory):
        
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            Checksum = FileChecksum(fname)

            if(Checksum in Duplicate):
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    Result = list(filter((lambda x: len(x)>1), Duplicate.values()))

    fobj.write("Duplicate files: \n")
    for value in Result:
        for subvalue in value:
            fobj.write(f"{subvalue}\n")

    fobj.close()

def main():
    
    fobj = open("log.txt","w")

    if(len(sys.argv) !=2 ):
        fobj.write("Invalid number of argumnets")
        return

    DirNm = sys.argv[1]
    DisplayDuplicate(DirNm)

    fobj.close()


if __name__ == "__main__":
    main()