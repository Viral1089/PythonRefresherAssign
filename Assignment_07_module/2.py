from datetime import datetime

class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance
        self.transactions = {}  # key: date, value: list of transactions for that date

    def _record_transaction(self, amount, description):
        today = datetime.now().strftime('%Y-%m-%d')
        if today not in self.transactions:
            self.transactions[today] = []
        self.transactions[today].append({'description': description, 'amount': amount})

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._record_transaction(amount, 'Deposit')

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient Balance.")
        self.balance -= amount
        self._record_transaction(-amount, 'Withdrawal')

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target account must be an instance of BankAccount.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        
        self.withdraw(amount)
        target_account.deposit(amount)
        self._record_transaction(-amount, f'Transfer to account {target_account.account_number}')
        target_account._record_transaction(amount, f'Transfer from account {self.account_number}')

    def calculate_interest(self, rate):
        if rate <= 0:
            raise ValueError("Interest rate must be positive.")
        interest = self.balance * (rate / 100)
        self.deposit(interest)
        return interest

    def get_balance(self):
        return self.balance

    def get_transactions(self, date=None):
        if date:
            return self.transactions.get(date, [])
        return self.transactions

    def __str__(self):
        return f'BankAccount(account_number={self.account_number}, owner={self.owner}, balance={self.balance})'

if __name__ == "__main__":
    account1 = BankAccount("123456", "Amit", 500)
    account2 = BankAccount("654321", "Aryan", 300)
    
    account1.deposit(200)
    account1.withdraw(100)
    account1.transfer(account2, 50)
    interest = account1.calculate_interest(5)  # 5% interest rate
    
    print(account1)
    print(account2)
    print("Account1 Transactions:", account1.get_transactions())
    print("Account2 Transactions:", account2.get_transactions())
    print("Interest Earned:", interest)
