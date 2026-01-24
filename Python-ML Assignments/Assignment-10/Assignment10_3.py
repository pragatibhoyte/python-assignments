def main():
    a=int(input("Enter a number: "))

    i=1
    factorial=1

    while(i<=a):
        factorial=factorial*i
        i+=1

    print(factorial)
    
if __name__ == "__main__":
    main()