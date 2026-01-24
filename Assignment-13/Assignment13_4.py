def BinaryEquivalent(No):
    binary=""
    while(No>0):
        Reminder=No%2
        binary=str(Reminder)+binary
        No=No//2
    
    print("Binary Euivalent : ",binary)

def main():
    num=int(input("Enter a number: "))
    BinaryEquivalent(num)
    

if __name__ == "__main__":
    main()