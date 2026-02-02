import threading

lock = threading.Lock()
Count = 0

def Counter(Data):
    global Count
    with lock:
        for i in Data:
            Count=Count+1
        
def main():
    
    Numbers = [0,1,2,3,4,5,6,7,8,9,10]
    
    Thread1 =threading.Thread(target=Counter,args=(Numbers,))
    Thread2 =threading.Thread(target=Counter,args=(Numbers,))
    Thread3 =threading.Thread(target=Counter,args=(Numbers,))

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

    print("Count is: ",Count)

if __name__ == "__main__":
    main()

