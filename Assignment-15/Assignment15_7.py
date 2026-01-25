from functools import reduce
def main():

    Data=["Pragati", "Neha", "Rutvik", "Yash", "Shubhman", "Virat"]
    print("Actual data is : ",Data)

    RData=list(filter((lambda str : (len(str)>5)), Data))
    print("Filtered data is : ",RData)

if __name__ == "__main__":
    main()