class BankAccount:
    ROI = 10.5

    def __init__(self, AccHolderName, AccBalance):

        self.Name = AccHolderName
        self.Balance = AccBalance
        
    def Display(self):
        print("Account Holder: ",self.Name) 
        print("Current Balance: ",self.Balance)

    def Deposit(self):
        Deposit = int(input("Enter Amount to deposit : "))
        self.Balance = self.Balance + Deposit

    def Withdraw(self):
        Amt = int(input("Enter amount to withdraw : "))
        if(self.Balance >= Amt):
            self.Balance = self.Balance - Amt
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        self.Interest = (self.Balance * BankAccount.ROI) / 100
        return self.Interest

def main():

    obj1 = BankAccount("Pragati Bhoyte", 10000)
    obj2 = BankAccount("Pooja Bhoyte", 10000)

    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

    print("-"*70)

    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()


if __name__ == "__main__":
    main()
