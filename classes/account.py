from classes.transaction import Transaction
from classes.exceptions import InsufficientFundsError, InvalidAmountError, SelfTransferError

# Klasa reprezentująca konto bankowe przypisane do użytkownika
# owner - właściciel konta (użytkownik User)
# balance - saldo początkowe konta
class Account:
    account_counter = 1000
    def __init__(self, owner, balance: float = 0.0):
        assert balance >= 0, "Saldo początkowe nie może być ujemne!"
        self.owner = owner
        self.balance = balance
        self.account_id = Account.account_counter
        self.transactions = []
        Account.account_counter += 1

    def deposit(self, amount: float, save: bool = True):
        if amount <= 0:
            raise InvalidAmountError("Kwota depozytu musi być dodatnia!")
        self.balance += amount
        if save: self.transactions.append(Transaction("deposit", amount))

    def withdraw(self, amount: float, save: bool = True):
        if amount <= 0:
            raise InvalidAmountError("Kwota wypłaty musi być dodatnia!")
        if self.balance < amount:
            raise InsufficientFundsError("Brak wystarczających środków!")
        self.balance -= amount
        if save: self.transactions.append(Transaction("withdraw", amount))

    def transfer_to(self, target_account, amount: float):
        if self == target_account:
            raise SelfTransferError("Nie można przelać na to samo konto!")
        self.withdraw(amount, False)
        target_account.deposit(amount, False)
        self.transactions.append(Transaction("transfer_to", amount, target_account.account_id))
        target_account.transactions.append(Transaction("transfer_from", amount, self.account_id))

    def filter_transactions(self, tx_type: str):
        return list(filter(lambda tx: tx.type == tx_type, self.transactions))
