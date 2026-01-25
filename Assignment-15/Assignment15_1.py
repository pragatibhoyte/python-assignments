def main():

    Data=[1,2,3,4,5,6]
    print("Actual data is : ",Data)

    MData=list(map((lambda no : no * no), Data))
    print("Mapped data is : ",MData)

if __name__ == "__main__":
    main()