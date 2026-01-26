def pattern(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j, end=" ")

        print()

def main():
        num=int(input("Enter Number : "))
        pattern(num)

if __name__ == "__main__":
    main()
