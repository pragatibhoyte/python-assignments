Divisibility = lambda No : (No%5==0)

def main():
    Num = int(input("Enter number : "))
    if(Divisibility(Num)):
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

if __name__ == "__main__":
    main()