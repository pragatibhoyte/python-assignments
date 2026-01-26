def Add(No1,No2):
    return No1+No2

def main():
    Num1=int(input("Enter first number : "))
    Num2=int(input("Enter second number : "))

    Result=Add(Num1,Num2)
    print(Result)

if __name__ == "__main__":
    main()