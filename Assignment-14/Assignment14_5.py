EvenOdd = lambda No : (No%2==0)

def main():
    Num = int(input("Enter number : "))
    if(EvenOdd(Num)):
        print("Even")
    else:
        print("Odd")
    
if __name__ == "__main__":
    main()