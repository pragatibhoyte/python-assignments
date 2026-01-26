def factorial(No):
    factorial=1
    for i in range(1,No+1):
            factorial=factorial*i
    return factorial
    
def main():
        num=int(input("Enter Number : "))
        print(factorial(num))

if __name__ == "__main__":
    main()
