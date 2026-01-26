def printStar(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Num=int(input("Enter a number : "))
    printStar(Num)

if __name__ == "__main__":
    main()