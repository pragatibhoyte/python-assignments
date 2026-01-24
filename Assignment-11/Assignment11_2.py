def count(n):
    count=0
    if(n==0):
        return 1
    while(n!=0):
        count+=1
        n = n // 10   # floor division:removes last number. for ex: 12/10=1.2 then 12//10=1

    return count

def main():
   number=int(input("Enter number: "))
   result=count(number)
   print(result)

if __name__ == "__main__":
    main()
