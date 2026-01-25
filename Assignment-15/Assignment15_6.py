from functools import reduce
def main():

    Data=[1,2,3,4,5,6]
    print("Actual data is : ",Data)

    RData=reduce((lambda A,B : B if A>B else A), Data)
    print("reduced data is : ",RData)

if __name__ == "__main__":
    main()