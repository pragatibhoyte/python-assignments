def CheckPerfectNo(no):
    Sum_div=0
    for i in range(1,no):
        if(no%i==0):
            Sum_div+=i
        
    if(Sum_div==no):
        print("Perfect number")
    else:
        print("Not perfect")

def main():
    num=int(input("Enter a number: "))
    CheckPerfectNo(num)

if __name__ == "__main__":
    main()