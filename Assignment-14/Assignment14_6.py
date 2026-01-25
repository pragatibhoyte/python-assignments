EvenOdd = lambda No : (No%2!=0)

def main():
    Num = int(input("Enter number : "))
    if(EvenOdd(Num)):
        print("Odd")
    else:
        print("Even")
    
if __name__ == "__main__":
    main()