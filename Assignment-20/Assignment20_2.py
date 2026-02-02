import threading

def EvenFactorFunction(number):
    print("Even Factors : ", end=" ")
    Total = 0
    for i in range(1,number):
        if(number % i == 0):
            if(i % 2 == 0):
                print(i, end=" ")
                Total+=i
    print("\nSum of Even Factors is : ",Total)

def OddFactorFunction(number):
    print("Odd Factors : ", end=" ")
    Total = 0
    for i in range(1,number):
        if(number % i == 0):
            if(i % 2 != 0):
                print(i, end=" ")
                Total+=i
    print("\nSum of Odd Factors is : ",Total)

def main():
    Number = 200

    EvenFactor = threading.Thread(target=EvenFactorFunction, args=(Number,))

    OddFactor = threading.Thread(target=OddFactorFunction, args=(Number,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")


if __name__ == "__main__":
    main()

