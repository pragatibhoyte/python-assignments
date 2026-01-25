def main():

    Data=[1,2,3,4,5,6]
    print("Actual data is : ",Data)

    FData=list(filter((lambda no : (no % 2!=0)), Data))
    print("Filtered data is : ",FData)

if __name__ == "__main__":
    main()