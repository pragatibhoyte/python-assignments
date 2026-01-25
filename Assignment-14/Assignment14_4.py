Minimum = lambda No1,No2 : No2 if No1>No2 else No1

def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))
    
    print("Smallest number : ",Minimum(Num1,Num2))
    
if __name__ == "__main__":
    main()