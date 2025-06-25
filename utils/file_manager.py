import os
import json
from cryptography.fernet import Fernet
from classes.user import User
from classes.account import Account
from classes.transaction import Transaction

# Tworzenie klucza do szyfrowania i deszyfrowania oraz zapisanie go do pliku, jeśli nie istnieje 
# lub załadowanie go z pliku, jeśli już istnieje
if not os.path.exists("data/secret.key"):
    key = Fernet.generate_key()
    os.makedirs(os.path.dirname("data/secret.key"), exist_ok=True)
    with open("data/secret.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("data/secret.key", "rb") as key_file:
        key = key_file.read()
fernet = Fernet(key)

# Funkcja zapisująca listę użytkowników i ich danych do pliku JSON
# users - lista użytkowników
# filename - nazwa pliku, w którym lista zostanie zapisana
def save_users_to_file(users, filename="data/bank_data.json"):
    data = []
    for user in users:
        user_data = {
            "user_id": user.user_id,
            "name": user.name,
            "password": user.password,
            "accounts": [
                {
                    "account_id": acc.account_id,
                    "balance": acc.balance,
                    "transactions": [tx.to_dict() for tx in acc.transactions],
                }
                for acc in user.accounts
            ],
        }
        data.append(user_data)
    
    encrypted = fernet.encrypt(json.dumps(data).encode())
    with open(filename, "wb") as f:
        f.write(encrypted)
    #with open(filename, "w", encoding="utf-8") as f:
    #    json.dump(data, f, indent=4)

# Funkcja wczytująca użytkowników i konta z pliku JSON
# filename - nazwa pliku, z którego lista zostanie wyczytana
def load_users_from_file(filename="data/bank_data.json"):
    users = []
    try:
        #with open(filename, "r", encoding="utf-8") as f:
        #    data = json.load(f)
        with open(filename, "rb") as f:
            encrypted = f.read()
        decrypted = fernet.decrypt(encrypted)
        data = json.loads(decrypted.decode())
    except FileNotFoundError:
        return []

    for u in data:
        user = User(u["user_id"], u["name"], u["password"])
        for acc_data in u["accounts"]:
            acc = Account(owner=user, balance=acc_data["balance"])
            acc.account_id = acc_data["account_id"]
            for tx_data in acc_data["transactions"]:
                tx = Transaction(
                    tx_data["type"],
                    tx_data["amount"],
                    tx_data["related_account"],
                )
                tx.date = tx_data["date"]
                acc.transactions.append(tx)
            user.accounts.append(acc)
        users.append(user)
    return users
