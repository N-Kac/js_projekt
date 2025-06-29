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

## Autorzy
- Kacper Nowak, 2ID13B
- Dominik Nowak, 2ID13B

## Wymagania

- Python 3.13+
- matplotlib (do wykresów)
- memory_profiler (testy pamięci)
- cryptography (szyfrowanie/deszyfrowanie)
- json (obsługa plików .json)
- datetime (pobieranie obecnej daty i godziny)
- unittest (do testowania)
- functools
- timeit (mierzenie czasu w teście wydajnościowym)

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

## Przykładowe dane
W pliku data/bank_data.json zostały przygotowane przykładowe dane.  
Użytkownicy i ich hasła:
```
1: Robert - hasło: admin
2: Adam - hasło: admin2
```

## Struktura modułów
```
js_projekt/
|
|-- main.py                 # Główna aplikacja (interfejs tekstowy)
|-- classes/                # Klasy
|   |-- __init__.py
|   |-- user.py             # Klasa User (użytkownik)
|   |-- account.py          # Klasa Account (konto)
|   |-- transaction.py      # Klasa Transaction (transakcja)
|   |-- exceptions.py       # Własne wyjątki
|
|-- utils/                  # Funkcje do obsługi plików i tworzenia wykresów
|   |-- __init__.py
|   |-- file_manager.py     # Zapis/odczyt z JSON używając szyfrowania i deszyfrowania
|   |-- data_visualizer.py  # Tworzenie i pokazywanie wykresów sald kont użytkowników
|
|-- tests/                  # Testy
|   |-- __init__.py
|   |-- test_accounts.py    # Testy z użyciem unittest
|   |-- test_memory.py      # Test pamięci memory_profiler
|
|-- data/                   # Folder, do którego zapisywane są dane .json, klucz oraz wykresy
|   |-- bank_data.json      # Plik, w którym przechowywani są użytkownicy, konta i transakcje
|   |-- secret.key          # Klucz do szyfrowania i deszyfrowania
|-- README.md               # Opis projektu
```