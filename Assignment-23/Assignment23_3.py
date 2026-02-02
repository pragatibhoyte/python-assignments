class Numbers:

    def __init__(self, No):
        self.Value = No
        
    def ChkPrime(self):
        if self.Value<=1:
            return False
        
        for i in range(2, self.Value):
            if (self.Value % i == 0):
                return False
        
        return True
    
    def ChkPerfect(self):
        Num = self.Value
        sum = 0
        for i in range(1, self.Value):
            if(self.Value % i == 0):
                sum+=i
        if(Num == sum):
            return True
        else:
            return False
        
    def Factors(self):
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                print(i, end=" ")
        print()
    
    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if(self.Value % i == 0):
                sum+=i
        return sum

def main():
   
    obj1 = Numbers(6)
    print("Is number perfect: ",obj1.ChkPerfect())
    print("Is number prime: ",obj1.ChkPrime())

    print("Factors : ",end="")
    obj1.Factors()

    print("Sum of Factors : ",obj1.SumFactors())

    No = int(input("Enter a number : "))
    obj2 = Numbers(No)
    print("Is number perfect: ",obj2.ChkPerfect())
    print("Is number prime: ",obj2.ChkPrime())

    print("Factors : ",end="")
    obj2.Factors()
    
    print("Sum of Factors : ",obj2.SumFactors())

if __name__ == "__main__":
    main()
