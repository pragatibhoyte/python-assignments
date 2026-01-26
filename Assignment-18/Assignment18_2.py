def main():
    no=int(input("Number of elememts : "))
    Data = []
    
    print("Input elements : ")
    for i in range(no):
        i=int(input())
        Data.append(i)
    
    Maximum=Data[0]
    
    for i in Data:
        if(Maximum<i):
            Maximum = i

    print("Output : ",Maximum)

if __name__ == "__main__":
    main()