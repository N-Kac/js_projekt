from memory_profiler import profile
from classes.user import User

# Test pamięci z wykorzystaniem memory_profiler: tworzenie użytkownika i 1000 kont
@profile
def memory_test_many_accounts():
    user = User(999, "TestPam", "securepass")
    for _ in range(1000):
        acc = user.create_account(100)
        acc.deposit(50)
        acc.withdraw(25)
    print(f"Liczba kont: {len(user.accounts)}")

if __name__ == "__main__":
    memory_test_many_accounts()
