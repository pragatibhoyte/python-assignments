def CountNo(No):
    count=0
    for i in No:
        count+=1
                  
    return count
    
def main():
        num=(input("Enter Number : "))
        print(CountNo(num))

if __name__ == "__main__":
    main()
