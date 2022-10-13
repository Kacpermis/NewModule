### 🔴 persystencja w praktyce

# Często programy na początku wczytują stan z poprzedniego uruchomienia, zmieniają ten stan i przed zakończeniem działania zapisują zmieniony stan do pliku.

### 🔴 Ćwiczenie

# Napisz kolejny program bazujący na todos.db.
# Program powinien jako argument przyjąć opis nowego zadania.
# Program ładuje do pamięci istniejącą bazę danych, dodaje nowe zadanie i zapisuje tak zmienioną listę zadań z powrotem do tego samego pliku.

import pickle
import sys

import click

DB_FILENAME = 'todos.db'

class TodoItem:
    def __init__(self, id, description, done):
        self.id = id
        self.description = description
        self.done = done
    
    def __eq__(self,other):
        return self.id == other.id and self.description == other.description and self.done == other.done
    
    def __repr__(self):
        return f"TodoItem(id={self.id!r}, description={self.description!r}, done={self.done!r})"

def next_id(todos):
    ids = {todo.id for todo in todos}
    counter = 1
    while counter in ids:
        counter += 1 
    return counter

@click.command()
@click.argument('description')
def main(description):
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    todo = TodoItem(
        id=next_id(todos),
        description=description,
        done=False
    )
    todos.append(todo)

    with open(DB_FILENAME, 'wb') as stream:
        pickle.dump(todos, stream)
    
    print('=ID= DONE? ==DESC==')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f'{todo.id:4} {done:^5} {todo.description}')

