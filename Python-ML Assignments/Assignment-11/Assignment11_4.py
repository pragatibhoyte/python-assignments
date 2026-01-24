def reverse(no):
    reverse=0
    while(no!=0):
        ld=no%10
        reverse=(reverse*10)+ld
        no=no//10
    return reverse

def main():
   number=int(input("Enter number: "))
   result=reverse(number)
   print(result)

if __name__ == "__main__":
    main()
