def ChkGreater():
    print("Enter first number:")
    a=input()
    print("Enter second number number:")
    b=input()

    if (a<b):
        print("Greater number is: ",b)
    else:
        print("Greater number is: ",a)

def main():
    ChkGreater()

if __name__ == "__main__":
    main()