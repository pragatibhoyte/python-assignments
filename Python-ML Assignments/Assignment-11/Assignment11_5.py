def reverse(no):
    num=no
    reverse=0
    while(no!=0):
        ld=no%10
        reverse=(reverse*10)+ld
        no=no//10
     
    if(num==reverse):
        return True

    return False

def main():
   number=int(input("Enter number: "))
   result=reverse(number)
   if (result):
        print("palindrome")
   else:
        print("not palindrome")

if __name__ == "__main__":
    main()
