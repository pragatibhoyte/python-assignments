def factor(no):
    for i in range(1,no+1):
        if(no%i==0):
            print(i)

def main():
    num=int(input("Enter a number: "))
    factor(num)

if __name__ == "__main__":
    main()