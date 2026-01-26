from functools import reduce

def main():
    Data =[]

    No=int(input("Enter Number of Elements : "))

    for i in range(No):
        i=int(input())
        Data.append(i)

    print("Input list = ",Data)

    FData = list(filter(lambda No: (No>=70 and No<=90), Data))
    print("List after filter =",FData)

    MData= list(map((lambda No : No+10), FData))
    print("List after map =",MData)

    RData = reduce((lambda A,B : A*B), MData)
    print("Output after reduce =",RData)

if __name__ == "__main__":
    main()