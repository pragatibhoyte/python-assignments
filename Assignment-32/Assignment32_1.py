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

def DirectoryChecksum(Directory):

    fobj = open("Ass1.log","w")

    if(os.path.exists(Directory) == False):
        fobj.write(f"{Directory} directory does not exist")
        return

    if(os.path.isdir(Directory) == False):
        fobj.write(f"{Directory} is not directory")
        return

    for FolderName, SubFolderName, FileName in os.walk(Directory):

        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            Checksum = FileChecksum(fname)

            fobj.write(f"File name: {fname} , Checksum : {Checksum}\n")

    fobj.close()

def main():
    
    fobj = open("Ass1.log","w")

    if(len(sys.argv) !=2 ):
        fobj.write("Invalid number of argumnets")
        return

    DirNm = sys.argv[1]
    DirectoryChecksum(DirNm)

    fobj.close()


if __name__ == "__main__":
    main()