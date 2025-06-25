from datetime import datetime

# Klasa przechowująca informacje o pojedynczej transakcji na koncie
# tx_type - typ transakcji ("deposit", "withdraw", "transfer_to", "transfer_from")
# amount - ilość pieniędzy
# related_account - konto użytkownika powiązanego z transakcją (dla przelewów)
class Transaction:
    def __init__(self, tx_type: str, amount: float, related_account: int = None):
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.type = tx_type
        self.amount = amount
        self.related_account = related_account

    def to_dict(self):
        return {
            "date": self.date,
            "type": self.type,
            "amount": self.amount,
            "related_account": self.related_account,
        }
