def DigitAddition(No):
    Addition = 0
    while(No>0):
        ld=No%10
        Addition+=ld
        No=No//10
    return Addition
        
def main(): 
        num=int(input("Enter Number : "))
        print(DigitAddition(num))

if __name__ == "__main__":
    main()
