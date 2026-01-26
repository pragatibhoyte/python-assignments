def main():
    a=int(input("Enter number: "))
    if(a%3==0 and a%5==0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")
   
if __name__ == "__main__":
    main()