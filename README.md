# Symulator Banku (Python)

## Cel projektu

Celem projektu było stworzenie prostego symulatora banku w Pythonie z:
- obsługą wielu użytkowników,
- kontami bankowymi,
- transakcjami (wpłata, wypłata, przelew),
- zapisem danych do pliku `.json`,
- filtrowaniem transakcji,
- prostym interfejsem tekstowym,
- testami,
- wizualizacją salda kont.

## Wymagania

- Python 3.13+
- matplotlib (do wykresów)
- memory_profiler (testy pamięci)
- json
- datetime
- unittest

Instalacja bibliotek:
```bash
pip install matplotlib
pip install memory_profiler
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
|   |-- file_manager.py     # Zapis/odczyt użytkowników, kont oraz transakcji z JSON
|   |-- data_visualizer.py  # Tworzenie wykresów i zapisywanie ich w plikach .png
|
|-- tests/
|   |-- __init__.py
|   |-- test_accounts.py    # Testy z użyciem unittest
|   |-- test_memory.py      # Test pamięci memory_profiler
|
|-- data/                   # Folder, do którego zpisywane są dane .json i wykresy
|-- README.md
```