import unittest
from classes.user import User
from classes.exceptions import InsufficientFundsError, InvalidAmountError, SelfTransferError
from utils.file_manager import save_users_to_file, load_users_from_file
import timeit

# Testy jednostkowe i graniczne metod klasy Account.
class TestAccountOperations(unittest.TestCase):
    def setUp(self):
        self.user1 = User(1, "Kacper", "nowak123")
        self.user2 = User(2, "Dominik", "nowak321")
        self.acc1 = self.user1.create_account(1000)
        self.acc2 = self.user2.create_account(500)

    # Test jednostkowy: wpłata na konto
    def test_deposit(self):
        self.acc1.deposit(200)
        self.assertEqual(self.acc1.balance, 1200)

    # Test jednostkowy: wypłata z konta
    def test_withdraw_success(self):
        self.acc1.withdraw(300)
        self.assertEqual(self.acc1.balance, 700)

    # Test graniczny: wypłata z konta większej ilości niż posiadana
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.acc1.withdraw(2000)

    # Test jednostkowy: przelew pomiędzy kontami
    def test_transfer_success(self):
        self.acc1.transfer_to(self.acc2, 400)
        self.assertEqual(self.acc1.balance, 600)
        self.assertEqual(self.acc2.balance, 900)

    # Test graniczny: przelew do tego samego konta
    def test_transfer_to_self(self):
        with self.assertRaises(SelfTransferError):
            self.acc1.transfer_to(self.acc1, 100)

    # Test graniczny: wpłata do konta o ujemnej wartości
    def test_negative_deposit(self):
        with self.assertRaises(InvalidAmountError):
            self.acc1.deposit(-100)

    # Test graniczny: wypłata z konta o wartości 0 PLN
    def test_zero_withdraw(self):
        with self.assertRaises(InvalidAmountError):
            self.acc1.withdraw(0)

    # Test jednostkowy: test funkcji filter_transactions
    def test_filter_transactions(self):
        self.acc1.deposit(100)
        self.acc1.deposit(150)
        deposits = self.acc1.filter_transactions("deposit")
        self.assertEqual(len(deposits), 2)
        self.assertTrue(all(tx.type == "deposit" for tx in deposits))

# Testy funkcjonalne, integracyjne, graniczne i wydajnościowe
class TestBankWorkflow(unittest.TestCase):
    # Test funkcjonalny: pełny scenariusz użytkownika
    def test_full_functional_flow(self):
        user = User(99, "TestUser", "pass")
        acc1 = user.create_account(1000)
        acc2 = user.create_account(500)
        acc1.withdraw(200)
        acc2.deposit(150)
        acc1.transfer_to(acc2, 300)
        self.assertEqual(acc1.balance, 500)
        self.assertEqual(acc2.balance, 950)
        self.assertEqual(len(acc2.transactions), 2)

    # Test integracyjny: zapis i odczyt danych
    def test_integration_save_and_load(self):
        user = User(88, "Integracyjny", "sekret")
        acc = user.create_account(1234)
        acc.deposit(66)
        save_users_to_file([user], filename="data/test_file.json")
        loaded = load_users_from_file("data/test_file.json")
        self.assertEqual(loaded[0].name, "Integracyjny")
        self.assertEqual(loaded[0].accounts[0].balance, 1300)

    # Test graniczny: przelew z pustego konta
    def test_edge_case_zero_balance_transfer(self):
        u1 = User(11, "Test", "1")
        u2 = User(12, "Graniczny", "2")
        acc1 = u1.create_account(0)
        acc2 = u2.create_account(100)
        with self.assertRaises(InsufficientFundsError):
            acc1.transfer_to(acc2, 1)

    # Test wydajności: tworzenie i operacje na wielu kontach
    def test_performance_many_accounts(self):
        start = timeit.default_timer()
        u = User(100, "Szybki", "fast")
        for _ in range(1000):
            acc = u.create_account(100)
            acc.deposit(50)
            acc.withdraw(25)
        stop = timeit.default_timer()
        duration = stop - start
        print(f"\nCzas wykonania dla 1000 kont: {duration:.4f}s")
        self.assertLess(duration, 2.0, "Za wolne (>2s)")

if __name__ == "__main__":
    unittest.main()
