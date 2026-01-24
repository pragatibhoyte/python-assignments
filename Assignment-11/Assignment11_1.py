def CheckPrime(no):
    if (no<=1):
        return False

    for i in range(2,no):
        if(no%i==0):
            return False

    return True

def main():
    n=int(input("Enter number: "))
    if CheckPrime(n):
        print("Prime number")
    else:
        print("Not prime number")

if __name__ == "__main__":
    main()
