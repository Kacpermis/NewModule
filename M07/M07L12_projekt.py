# Napisz program, który ułatwi milionom Polaków śledzenie własnych wydatków oraz ich analizę. Program pozwala na łatwe dodawanie nowych wydatków i generowanie raportów. Aplikacja działa także pomiędzy uruchomieniami, przechowując wszystkie dane w pliku. Każdy wydatek ma id, opis oraz wielkość kwoty.

# 1. Program posiada podkomendy add, report, export-python oraz import-csv. 

# 2. Podkomenda add pozwala na dodanie nowego wydatku. Należy wówczas podać jako kolejne argumenty wiersza poleceń wielkość wydatku (jako int) oraz jego opis (w cudzysłowach). Na przykład:
# $ python budget.py add 100 "stówa na zakupy". 
# Jako id wybierz pierwszy wolny id - np. jeśli masz już wydatki z id = 1, 2, 4, 5, wówczas wybierz id = 3.

# 3. Podkomenda report wyświetla wszystkie wydatki w tabeli. W tabeli znajduje się także kolumna "big?", w której znajduje się ptaszek, gdy wydatek jest duży, tzn. co najmniej 1000. Dodatkowo, na samym końcu wyświetlona jest suma wszystkich wydatów.

# 4. Podkomenda export-python wyświetla listę wszystkich wydatków jako obiekt (hint: zaimplementuj poprawnie metodę __repr__ w klasie reprezentującej pojedynczy wydatek).

# 5. Podkomenda import-csv importuję listę wydatków z pliku CSV.

# 6. Program przechowuje pomiędzy uruchomieniami bazę wszystkich wydatków w pliku budget.db. Zapisuj i wczytuj stan używając modułu pickle. Jeżeli plik nie istnieje, to automatycznie stwórz nową, pustą bazę. Zauważ, że nie potrzebujemy podpolecenia init.

# 7. Wielkość wydatku musi być dodatnią liczbą. Gdzie umieścisz kod sprawdzający, czy jest to spełnione? W jaki sposób zgłosisz, że warunek nie jest spełniony?
import csv
from pickle import load, dump
import sys

from dataclasses import dataclass
import click


DB_FILENAME = "budget.db"
BIG_EXPENSE = 1000

@dataclass
class Expenses:
    id: int
    amount: float
    description: str

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError('Amount cannot be zero or less')
    
    def is_big(self):
        return self.amount >= BIG_EXPENSE


def read_or_init():
    try:
        with open(DB_FILENAME, 'rb') as stream:
            expenses = load(stream)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_db(expenses):
    with open(DB_FILENAME, 'wb') as stream:
        expenses = dump(expenses, stream)

def new_id(expenses):
    ids = {expense.id for expense in expenses}
    counter = 1
    while counter in ids:
        counter += 1 
    return counter

def total_expenses(expenses):
    amounts = [e.amount for e in expenses]
    return sum(amounts)

def print_expenses(expenses, total_expenses):
    print(f'--ID-- -AMOUTNT- -BIG?- --DESCRIPTION-------')
    for expense in expenses:
        if expense.is_big():
            big = "(!)"
        else:
            big = ""
        print(f'{expense.id:4} {expense.amount:10} {big:^8} {expense.description:^8}')
    print(f"TOTAL: {total_expenses:8}")


@click.group()
def cli():
    pass

@cli.command()
def report():
    expenses = read_or_init()
    total = total_expenses(expenses)
    print_expenses(expenses, total)


    