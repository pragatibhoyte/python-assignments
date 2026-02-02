import threading

def is_prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def PrimeFun(Data):
    print("Prime numbers:", end=' ')
    for i in Data:
        if(is_prime(i)==True):
            print(i, end=" ")
    print()

def NonPrimeFun(Data):
    print("Non Prime numbers:", end=' ')
    for i in Data:
        if(is_prime(i)==False):
            print(i, end=" ")
    print()
        
def main():

    Numbers = [1,2,3,4,5,6,7,8,9]

    Prime = threading.Thread(target=PrimeFun, args=(Numbers,))
    NonPrime = threading.Thread(target=NonPrimeFun, args=(Numbers,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()

if __name__ == "__main__":
    main()

