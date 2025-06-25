import sys
from classes.user import User
from classes.exceptions import InsufficientFundsError, InvalidAmountError, SelfTransferError
from utils.file_manager import load_users_from_file, save_users_to_file
from utils.data_visualizer import plot_account_balances, plot_user_account_balances

users = load_users_from_file()

# Funkcja pozwalająca znaleźć użytkownika o podanym ID (uid), jeśli istnieje
def find_user_by_id(uid):
    for u in users:
        if u.user_id == uid:
            return u
    return None

# Funckja menu głównego pozwalająca użytkownikowi zalogować i zarejestrować się z hasłem 
# oraz wygenerować wykres sald wszystkich użytkowników
def main_menu():
    while True:
        print("\n--- DOSTĘPNI UŻYTKOWNICY ---")
        if not users:
            print("Brak użytkowników!")
        else:
            for u in users:
                print(f"{u.user_id}: {u.name}")

        print("\n--- MENU GŁÓWNE ---")
        print("[1] ZALOGUJ DO ISTNIEJĄCEGO UŻYTKOWNIKA")
        print("[2] STWÓRZ NOWEGO UŻYTKOWNIKA")
        print("[3] WYGENERUJ WYKRES DLA WSZYSTKICH UŻYTKOWNIKÓW")
        print("[0] WYJŚCIE")
        option = input("OPCJA: ")

        if option == '1':
            if not users:
                print("Brak użytkowników!")
                continue

            print("--- LOGOWANIE DO UŻYTKOWNIKA ---")
            uid_in = input("ID Użytkownika: ")
            if not uid_in.isdigit():
                print("ID musi być liczbą całkowitą!")
                continue
            uid = int(uid_in)

            user = find_user_by_id(uid)
            if not user:
                print("Nieprawidłowe ID!")
                continue

            for _ in range(3):
                password = input("Hasło: ")
                if password == user.password:
                    return user
                print("Nieprawidłowe hasło!\n")
            print("Za dużo nieudanych prób logowania! Zamykanie programu...")
            sys.exit()
        elif option == '2':
            print("--- TWORZENIE NOWEGO UŻYTKOWNIKA ---")
            name = input("Nazwa: ")
            password = input("Hasło: ")
            new_user = User(len(users) + 1, name, password)
            users.append(new_user)
            return new_user
        elif option == '3':
            plot_account_balances(users)
            continue
        elif option == '0':
            print("\nZamykanie programu...")
            sys.exit()
        else:
            print("Nieprawidłowa opcja!")

def show_accounts(user):
    print(f"--- KONTA UŻYTKOWNIKA {user.name} ---")
    if not user.accounts:
        print("Brak kont!")
        return False

    account_info = [(acc.account_id, acc.balance) for acc in user.accounts]
    for acc_id, bal in account_info:
        print(f"ID: {acc_id} | Saldo: {bal:.2f} PLN")
    return True

# Funkcja rekurencyjna pozwalająca wybrać konto użytkownika po ID, jeśli istnieje
# Jeśli przekazany user to None, szuka po wszystkich użytkownikach
def select_account(user, prompt="ID Konta: "):
    if user and not show_accounts(user):
        return None

    acc_id = 0
    while True:
        try:
            acc_id = int(input(prompt))
            break
        except ValueError:
            print("ID musi być liczbą całkowitą!")
            return select_account(user, prompt)

    search_in = user.accounts if user else [acc for u in users for acc in u.accounts]
    for acc in search_in:
        if acc.account_id == acc_id:
            return acc
    print("Nie znaleziono konta!")
    return select_account(user, prompt)

# Funkcja pobierająca i walidująca wprowadzoną przez użytkownika ilość pieniędzy
def get_valid_amount(prompt="Kwota: "):
    while True:
        val = input(prompt)
        try:
            return float(val)
        except ValueError:
            print("Kwota musi być liczbą!")

# Funkcja wyświetlająca interaktywne menu użytkownika i obsługująca rózne operacje
# (np. założenie nowego konta, wyświetlenie transkacji danego konta)
def user_menu(user):
    while True:
        print(f"\n--- MENU UŻYTKOWNIKA {user.name} ---")
        print("[1] ZAŁÓŻ KONTO")
        print("[2] WYŚWIETL KONTA")
        print("[3] WPŁAĆ NA KONTO")
        print("[4] WYPŁAĆ Z KONTA")
        print("[5] WYKONAJ PRZELEW")
        print("[6] WYŚWIETL TRANSAKCJE KONTA")
        print("[7] WYGENERUJ WYKRES")
        print("[8] WYŚWIETL ŁĄCZNE SALDO")
        print("[9] WYSZUKAJ TRANSAKCJE")
        print("[0] WYLOGUJ")

        choice = input("OPCJA: ")
        if choice == '1':
            print("--- TWORZENIE NOWEGO KONTA ---")
            again = input("Czy jesteś pewien? (T/N): ").strip().lower()
            if again != 't':
                continue
            acc = user.create_account()
            print(f"Utworzono konto o ID {acc.account_id}!")
            save_users_to_file(users)
        elif choice == '2':
            show_accounts(user)
        elif choice == '3':
            acc = select_account(user)
            amount = get_valid_amount("Kwota wpłaty: ")
            try:
                acc.deposit(amount)
                print("Wpłata wykonana pomyślnie!")
                save_users_to_file(users)
            except InvalidAmountError as e:
                print(e)
        elif choice == '4':
            acc = select_account(user)
            amount = get_valid_amount("Kwota wypłaty: ")
            try:
                acc.withdraw(amount)
                print("Wypłata wykonana pomyślnie!")
                save_users_to_file(users)
            except (InvalidAmountError, InsufficientFundsError) as e:
                print(e)
        elif choice == '5':
            acc_from = select_account(user)
            target_acc = select_account(None, "ID Konta docelowego: ")
            amount = get_valid_amount("Kwota przelewu: ")
            try:
                acc_from.transfer_to(target_acc, amount)
                print("Przelew wykonany pomyślnie!")
                save_users_to_file(users)
            except (InvalidAmountError, InsufficientFundsError, SelfTransferError) as e:
                print(e)
        elif choice == '6':
            acc = select_account(user)
            print()
            for tx in acc.transactions:
                print(f"{tx.date} | {tx.type} | {tx.amount:.2f} | {tx.related_account or '-'}")
        elif choice == '7':
            plot_user_account_balances(user)
        elif choice == '8':
            print(f"Łączne saldo użytkownika: {user.total_balance():.2f} PLN")
        elif choice == '9':
            acc = select_account(user)
            valid_types = {"deposit", "withdraw", "transfer_to", "transfer_from"}
            tx_type = input("Typ transakcji (deposit, withdraw, transfer_to, transfer_from): ").lower()
            if tx_type not in valid_types:
                print("Nieprawidłowy typ transakcji!")
                continue

            transactions = acc.filter_transactions(tx_type)
            if not transactions:
                print("\nNie znaleziono takich transakcji!")
            else:
                print()
                for tx in transactions:
                    print(f"{tx.date} | {tx.type} | {tx.amount:.2f} | {tx.related_account or '-'}")
        elif choice == '0':
            break
        else:
            print("Nieprawidłowa opcja!")

# Główna pętla programu
if __name__ == "__main__":
    while True:
        print("\n=== SYMULATOR BANKU ===")
        current_user = main_menu()
        user_menu(current_user)
        again = input("Wrócić do menu głównego? (T/N): ").strip().lower()
        if again != 't':
            break
