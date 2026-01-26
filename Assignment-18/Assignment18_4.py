def main():
    no=int(input("Number of elememts : "))
    Data = []
    
    print("Input elements : ")
    for i in range(no):
        i=int(input())
        Data.append(i)

    SearchEle=int(input("Element to search : "))
    count=0
    
    for i in Data:
        if(SearchEle==i):
            count+=1

    print("Output : ",count)

if __name__ == "__main__":
    main()