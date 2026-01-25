Maximum = lambda No1,No2 : No1 if No1>No2 else No2

def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))
    
    print("Largest number : ",Maximum(Num1,Num2))
    
if __name__ == "__main__":
    main()