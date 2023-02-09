class BankAccount:
    def __init__(self, account_number, account_balance, interst_rate):
        self.account_number = account_number
        self.account_balance = account_balance
        self.interst_rate = interst_rate

    # returns the account information
    def __repr__(self):
        return f"Account Number: {self.account_number}, Account Balance: {self.account_balance}, Interest Rate: {self.interst_rate}"


account = BankAccount(123456789, 8.00, 0.05)
print(account.account_number)
print(account.account_balance)
print(account.interst_rate)
