def pattern(No):
    for i in range(No):
        for j in range(No):
            print("*", end=" ")

        print()

def main():
        num=int(input("Enter Number : "))
        pattern(num)

if __name__ == "__main__":
    main()
