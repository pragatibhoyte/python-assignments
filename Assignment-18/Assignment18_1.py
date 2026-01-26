def main():
    no=int(input("Number of elememts : "))
    Data = []
    Addition=0
    print("Input elements : ")
    for i in range(no):
        i=int(input())
        Data.append(i)
    
    for i in Data:
        Addition+=i

    print("Output : ",Addition)

if __name__ == "__main__":
    main()