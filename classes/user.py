from functools import reduce
from classes.account import Account

# Klasa reprezentująca użytkownika systemu bankowego
# user_id - identyfikator użytkownika
# name - nazwa użytkownika
# password - hasło użytkownika
class User:
    def __init__(self, user_id: int, name: str, password: str):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.accounts = []

    def create_account(self, initial_balance: float = 0.0):
        account = Account(self, initial_balance)
        self.accounts.append(account)
        return account

    def total_balance(self):
        return reduce(lambda acc_sum, acc: acc_sum + acc.balance, self.accounts, 0)
