def main():

    Data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print("Actual data is : ",Data)

    count=0
    FData=list(filter((lambda no : (no%2==0)), Data))
    for no in FData:
        count+=1
    print("Count of even numbers is : ",count)

if __name__ == "__main__":
    main()