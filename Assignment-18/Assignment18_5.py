import MarvellousNum

def ListPrime(No):
    Data = []
    for i in range(0,No):
        i=int(input())
        Data.append(i)

    Addition = 0

    for i in Data:
        if(MarvellousNum.ChkPrime(i)):
            Addition+=i

    print("Output : ",Addition)

def main():
    no=int(input("Number of elememts : "))
    ListPrime(no)

if __name__ == "__main__":
    main()