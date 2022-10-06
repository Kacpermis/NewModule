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
        description=row['desc'],
        done=(row['done'] == 'x'),
    )


def description(todos):
    print("  ID  DONE? DESCRIPTION")
    print('---- ----- ------------')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f"{todo.id:6d} {done:^5} {todo.description}")
    
def summary(todos):
    done = len([t for t in todos if t.done])
    all_ = len(todos)

    print()
    print(f"Number of fullfiled tasks: {done}/{all_}")

def main():
    todos = read_toDo(TODOS_FILENAME)
    description(todos)
    summary(todos)

if __name__ == "__main__":
    main()
