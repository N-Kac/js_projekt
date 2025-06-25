import matplotlib.pyplot as plt

# Generuje wykres słupkowy sald kont wszystkich użytkownika i zapisuje do PNG
# user - użytkownik
# save_path - nazwa pliku, w którym wykres zostanie zapisany
def plot_account_balances(users, save_path="data/salda_uzytkownikow.png"):
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
    plt.savefig(save_path)
    print(f"Wykres sald użytkowników został zapisany jako '{save_path}'.")
    plt.close()

# Generuje wykres słupkowy sald kont danego użytkownika i zapisuje do PNG
# user - użytkownik
# save_path - nazwa pliku, w którym wykres zostanie zapisany
def plot_user_account_balances(user, save_path=None):
    labels = list(map(lambda acc: f"{user.name}-{acc.account_id}", user.accounts))
    balances = list(map(lambda acc: acc.balance, user.accounts))

    if not save_path:
        save_path = f"data/saldo_{user.name.lower()}.png"
    bars = plt.bar(labels, balances)

    # Dodawanie wartości nad każdym słupkiem
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, f"{yval:.2f}", ha='center', va='bottom', fontsize=9)

    plt.title(f"Salda kont użytkownika {user.name}")
    plt.xlabel("Konto")
    plt.ylabel("Saldo [PLN]")
    plt.savefig(save_path)
    print(f"Wykres sald użytkownika '{user.name}' został zapisany jako '{save_path}'.")
    plt.close()
