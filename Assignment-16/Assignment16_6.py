def printNo(No):
    if(No<0):
        print("Negative Number")
    elif(No>0):
        print("Positive Number")
    elif(No==0):
        print("Zero")

def main():
    Num=int(input("Enter a number : "))
    printNo(Num)

if __name__ == "__main__":
    main()