import threading

def Numbers(no):
    for i in range(1,no+1):
        print(i, end=" ")

    print()

def reverse(no):
    for i in range(no,0,-1):
        print(i ,end=" ")

    print()


def main():
    Number = 50

    Thread1= threading.Thread(target = Numbers, args=(Number,))
    Thread2= threading.Thread(target = reverse, args=(Number,))

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()


if __name__ == "__main__":
    main()

