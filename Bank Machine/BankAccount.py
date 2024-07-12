class BankAccount:

    def __init__(self, account_holder, pin, balance=0) -> None:
        self.account_holder = account_holder
        self.pin = str(pin)
        self.balance = float(balance)
        self.overdraft_status = False
    
    def set_overdraft_status(self):
        if self.balance < 0:
            self.overdraft_status = True
        else:
            self.overdraft_status = False
    
    def get_overdraft_status(self):
        return self.overdraft_status
    
    def get_pin(self):
        return self.pin
    
    def get_account_holder(self):
        return self.account_holder
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.set_overdraft_status()
            return "Deposit successful!"
        else:
            return "The deposit must be more than EUR 0."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.set_overdraft_status()
            return "Withdraw successful!"
        else:
            return "The withdraw must be more than EUR 0 and less or equal than your account balance."