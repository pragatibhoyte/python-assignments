from functools import reduce

def ChkPrime(No):
    
    if (No <=1):
        return False
    
    for i in range(2,No):
        if(No % i == 0):
            return False
        
    return True
def main():
    Data =[]

    No=int(input("Enter Number of Elements : "))

    for i in range(No):
        i=int(input())
        Data.append(i)

    print("Input list = ",Data)

    FData = list(filter(ChkPrime, Data))
    print("List after filter =",FData)

    MData= list(map((lambda No : No*2), FData))
    print("List after map =",MData)

    RData = reduce((lambda A,B : A if A>B else B), MData)
    print("Output after reduce =",RData)

if __name__ == "__main__":
    main()