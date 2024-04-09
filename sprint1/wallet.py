class Wallet:

    # first thing to run when we make a new class
    # outline required user-provided input values
    # parameters with default values assigned are option e.g def __init__(self, initial_amount=0)
    def __init__(self, initial_amount = 0):
        # save the user-provided initial_amounut
        self.balance = initial_amount
    
    # spend cash method
    def spend_cash(self, amount):
        if self.balance < amount:
            return "not enough  money"
        else:
            self.balance = self.balance - amount
            return f"remaining balance: {self.balance}"
    
    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f"new balance of: {self.balance}"

    # __repr__ method changes how the object looks when it is printed out
    # the self  helps tp modify attributes within this function
    def __repr__(self):
        return f"wallet with balanceof: {self.balance}"

if __name__=='__main__':
    wallet1 = Wallet(100)
    wallet2 = Wallet(50)
    wallet3 = Wallet(3000)
    print(wallet1)
    print(wallet2)
    print(wallet3)