### 🔴 Praca z plikami CSV

# Dane są często przechowywane w plikach CSV. Można je ręcznie przetwarzać używając metody .split("\n") oraz .split(","), ale prościej jest wykorzystać wbudowaną bibliotekę csv.

# Dostarcza ona klasy DictReader, dzięki czemu każdy wiersz otrzymamy jako SŁOWNIK mapujący z nazwy kolumny na wartość. Na przykład:

import csv

# with open("M06/expenses.csv") as stream:
#     reader = csv.DictReader(stream)  # Od tego momentu już nie operujemy bezpośrednio na strumieniu, tylko na readerze.
#     for row in reader:  # Ten fragment musi byc zagnieżdżony, bo reader na bieżąco odczytuje plik linia po linii!
#         print(row)

### 🔴 Ćwiczenie

# Napisz program służący do zarządzania listą zadań do wykonania (todolist).

# Program powinien wczytać listę zadań z pliku CSV takiego jak todos.csv, a następnie wyświetlić wszystkie zadania w tabeli, a także podsumowanie ile zadań jest już wykonanych.

# Każde zadanie składa się z id, opisu oraz informacji, czy zadanie zostało już wykonane (znak 'x'), czy jeszcze nie (znak '-').
import csv
TODOS_FILENAME = 'M06\\todos.csv'

class TodoItem:
    def __init__(self, id, description, done):
        self.id = id
        self.description = description
        self.done = done

def read_toDo(filename):
    with open(filename) as stream:
        read = csv.DictReader(stream)
        todos = [ToDoItem_from_dict(row) for row in read]
    return todos

def ToDoItem_from_dict(row):
    return TodoItem(
        id=int(row['id']),
        description=row(['desc']),
        done=(row['done'] == 'x'),
    )


def description():
    print("  ID  DONE? DESCRIPTION")
    print('---- ----- ------------')

def main():
    read_toDo()
    description()

if __name__ == "__main__":
    main()
