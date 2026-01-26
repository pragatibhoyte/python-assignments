def CheckPrime(No):
    if(No<=1):
        return False
    for i in range(2,No):
        if(No%i==0):
            return False
        
    return True
        
def main():
        num=int(input("Enter Number : "))
        if(CheckPrime(num)):
            print("It is prime number")
        else:
            print("It is not prime number")

if __name__ == "__main__":
    main()
