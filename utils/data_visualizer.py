import matplotlib.pyplot as plt

# Generuje wykres słupkowy sald kont wszystkich użytkownika i zapisuje do PNG
# users - lista użytkowników
# save_path - nazwa pliku, do którego zostanie zapisany wkyres
def plot_account_balances(users, save_path="data/salda_uzytkownikow.png"):
    fig = plt.figure(num="Salda kont użytkowników")
    labels = list(map(lambda user: user.name, users))
    balances = list(map(lambda user: user.total_balance(), users))
    bars = plt.bar(labels, balances)

    # Dodawanie wartości nad każdym słupkiem
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f"{yval:.2f}", ha='center', va='bottom', fontsize=9)

    plt.title("Salda kont użytkowników")
    plt.xlabel("Konto")
    plt.ylabel("Saldo [PLN]")

    # Pokazanie wykresu
    plt.tight_layout()
    plt.show()

    # Zapytanie użytkownika czy chce zapisać do pliku
    save = input("Czy zapisać wykres do pliku? (T/N): ").strip().lower()
    if save == 't':
        fig.savefig(save_path)
        print(f"Wykres został zapisany jako '{save_path}'.")

    plt.close()

# Generuje wykres słupkowy sald kont danego użytkownika i zapisuje do PNG
# user - użytkownik
# save_path - nazwa pliku, do którego zostanie zapisany wkyres
def plot_user_account_balances(user, save_path=None):
    fig = plt.figure(num=f"Salda kont użytkownika {user.name}")
    labels = list(map(lambda acc: f"{user.name}-{acc.account_id}", user.accounts))
    balances = list(map(lambda acc: acc.balance, user.accounts))

    bars = plt.bar(labels, balances)

    # Dodawanie wartości nad każdym słupkiem
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, f"{yval:.2f}", ha='center', va='bottom', fontsize=9)

    plt.title(f"Salda kont użytkownika {user.name}")
    plt.xlabel("Konto")
    plt.ylabel("Saldo [PLN]")

    # Pokazanie wykresu
    plt.tight_layout()
    plt.show()

    if not save_path:
        save_path = f"data/saldo_{user.name.lower()}.png"
    # Zapytanie użytkownika czy chce zapisać do pliku
    save = input("Czy zapisać wykres do pliku? (T/N): ").strip().lower()
    if save == 't':
        fig.savefig(save_path)
        print(f"Wykres został zapisany jako '{save_path}'.")

    plt.close()
