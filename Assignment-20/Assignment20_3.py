import threading

def EvenListFunction(Data):
    print("Even elements : ", end="")
    Total = 0
    for i in Data:
        if(i % 2 == 0):
            print(i, end=" ")
            Total+=i
    print("\nSum of Even elements : ",Total)

def OddListFunction(Data):
    print("Odd elements : ", end="")
    Total = 0
    for i in Data:
        if(i % 2 != 0):
            print(i, end=" ")
            Total+=i
    print("\nSum of Odd elements : ",Total)

def main():
    Numbers = [1,2,3,4,5,6,7,8,9]

    EvenFactor = threading.Thread(target=EvenListFunction, args=(Numbers,))

    OddFactor = threading.Thread(target=OddListFunction, args=(Numbers,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

