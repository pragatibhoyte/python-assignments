def main():
    no=int(input("Number of elememts : "))
    Data = []
    
    print("Input elements : ")
    for i in range(no):
        i=int(input())
        Data.append(i)
    
    Minimum=Data[0]
    
    for i in Data:
        if(Minimum>i):
            Minimum = i

    print("Output : ",Minimum)

if __name__ == "__main__":
    main()