import threading

def SmallLetter(Data):
    Total = 0

    for i in Data:
        if(i.islower()):
            Total+=1

    print("Thread ID : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)
    print("Total Small letters : ",Total)
    print()

def CapitalLetter(Data):
    Total = 0

    for i in Data:
        if(i.isupper()):
            Total+=1

    print("Thread ID : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)
    print("Total Capital letters : ",Total)
    print()

def DigitCount(Data):
    Total = 0

    for i in Data:
        if(i.isdigit()):
            Total+=1

    print("Thread ID : ",threading.get_ident())
    print("Thread name : ",threading.current_thread().name)
    print("Total digits : ",Total)
    print()

def main():

    String= "PragatiBhoyte73"

    Small = threading.Thread(target=SmallLetter,args=(String,))
    Capital = threading.Thread(target=CapitalLetter, args=(String,))
    Digits = threading.Thread(target=DigitCount, args=(String,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main thread", threading.get_ident())

if __name__ == "__main__":
    main()

