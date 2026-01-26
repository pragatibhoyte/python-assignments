def AddFactors(No):
    Addition=0
    for i in range(1,No):
        if(No%i==0):
             Addition+=i
                  
    return Addition
    
def main():
        num=int(input("Enter Number : "))
        print(AddFactors(num))

if __name__ == "__main__":
    main()
