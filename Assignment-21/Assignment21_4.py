import threading

def Addition(Data):
    Sum=0
    for i in Data:
        Sum=Sum+i
    print("Addition is :",Sum)

def Multiplication(Data):
    Product=1
    for i in Data:
        Product=Product*i
    print("Multiplication is :",Product)
        
def main():
    
    Numbers = [1,2,3,4,5,6,7,8,9,10]
    
    Thread1 =threading.Thread(target = Addition ,args=(Numbers,))
    Thread2 =threading.Thread(target = Multiplication ,args=(Numbers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()

