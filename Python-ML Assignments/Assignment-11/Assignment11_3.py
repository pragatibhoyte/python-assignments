def SumDigit(n):
    SumDigit=0
    
    while(n!=0):
        LastDigit = n % 10
        SumDigit=SumDigit+LastDigit
        n=n//10

    return SumDigit

def main():
   number=int(input("Enter number: "))
   result=SumDigit(number)
   print(result)

if __name__ == "__main__":
    main()
