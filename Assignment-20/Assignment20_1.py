import threading

def SumEven():
    i=1
    no = 2*10
    print("Even numbers : ")
    while(no>0):
        if(i % 2 == 0):
            print(i, end='\t' )
        i+=1
        no=no-1
    print(" ")

def SumOdd():
    i=1
    no = 2*10
    print("Odd numbers : ")
    while(no>0):
        if(i % 2 != 0):
            print(i, end='\t' )
        i+=1
        no=no-1
    print(" ")


def main():
    
    Even = threading.Thread(target=SumEven)
    Odd = threading.Thread(target=SumOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()
