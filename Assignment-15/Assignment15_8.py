def main():

    Data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print("Actual data is : ",Data)

    FData=list(filter((lambda no : (no%3==0 and no%5==0)), Data))
    print("Filtered data is : ",FData)

if __name__ == "__main__":
    main()