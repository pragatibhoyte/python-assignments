import Arithmatic as Ar
def main():
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))

    print("Addition = ",Ar.Add(num1,num2))
    print("Subtraction = ",Ar.Sub(num1,num2))
    print("Multiplication = ",Ar.Mult(num1,num2))
    print("Division",Ar.Div(num1,num2))

if __name__ == "__main__":
    main()
