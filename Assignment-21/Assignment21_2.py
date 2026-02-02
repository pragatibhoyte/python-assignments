import threading

def Max_ele(Data):
    Maximum = Data[0]
    for i in Data:
        if(Maximum<i):
            Maximum=i
    print("Maximum Element : ",Maximum)

def Min_ele(Data):
    Minimum = Data[0]
    for i in Data:
        if(Minimum>i):
            Minimum=i
    print("Minimum Element : ",Minimum)
        
def main():

    Nos=list(map(int,input("Enter the List Elements : ").split()))
    
    Thread1 =threading.Thread(target=Max_ele, args=(Nos,))
    Thread2 =threading.Thread(target=Min_ele, args=(Nos,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()

