class Arithmatic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter value 1 : "))
        self.Value2 = int(input("Enter value 2 : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Cannot divide by zero"
        else:
            return self.Value1 / self.Value2


def main():
    obj1 = Arithmatic()
    obj2 = Arithmatic()

    obj1.Accept()
    print("Addition : ",obj1.Addition())
    print("Subtraction: ",obj1.Subtraction())
    print("Multiplication: ",obj1.Multiplication())
    print("Division : ",obj1.Division())

    obj2.Accept()
    print("Addition : ",obj2.Addition())
    print("Subtraction : ",obj2.Subtraction())
    print("Multiplication: ",obj2.Multiplication())
    print("Division : ",obj2.Division())

if __name__ == "__main__":
    main()


