# Wyjątek: brak wystarczających środków
class InsufficientFundsError(Exception):
    pass

# Wyjątek: zła kwota (np. < 0)
class InvalidAmountError(Exception):
    pass

# Wyjątek: przelew na własne konto
class SelfTransferError(Exception):
    pass
