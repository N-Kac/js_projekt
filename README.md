# Symulator Banku (Python)

## Cel projektu

Celem projektu było stworzenie prostego symulatora banku w Pythonie z:
- obsługą wielu użytkowników,
- kontami bankowymi,
- transakcjami (wpłata, wypłata, przelew),
- zapisem danych do pliku `.json` (z szyfrowaniem i deszyfrowaniem),
- filtrowaniem transakcji,
- prostym interfejsem tekstowym,
- testami,
- wizualizacją salda kont.

## Wymagania

- Python 3.13+
- matplotlib (do wykresów)
- memory_profiler (testy pamięci)
- cryptography (szyfrowanie/deszyfrowanie)
- json
- datetime
- unittest

Instalacja bibliotek:
```bash
pip install matplotlib
pip install memory_profiler
pip install cryptography
```

## Uruchamianie
```bash
python main.py
```

## Uruchamianie testów
```bash
python -m unittest tests/test_accounts.py
python -m memory_profiler tests/test_memory.py
```

## Struktura modułów
```
js_projekt/
|
|-- main.py                 # Główna aplikacja (interfejs tekstowy)
|-- classes/
|   |-- __init__.py
|   |-- user.py             # Klasa User
|   |-- account.py          # Klasa Account
|   |-- transaction.py      # Klasa Transaction
|   |-- exceptions.py       # Własne wyjątki
|
|-- utils/
|   |-- __init__.py
|   |-- file_manager.py     # Zapis/odczyt z JSON używając szyfrowania i deszyfrowania
|   |-- data_visualizer.py  # Tworzenie i pokazywanie wykresów sald kont użytkowników
|
|-- tests/
|   |-- __init__.py
|   |-- test_accounts.py    # Testy z użyciem unittest
|   |-- test_memory.py      # Test pamięci memory_profiler
|
|-- data/                   # Folder, do którego zapisywane są dane .json i klucz
|   |-- secret.key          # Klucz do szyfrowania i deszyfrowania
|-- README.md
```