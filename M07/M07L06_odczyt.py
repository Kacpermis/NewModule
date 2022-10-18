### 🔴 pickle - odczyt

# Jak wczytać dane z pliku data.db z poprzedniej lekcji?

# import pickle

# filename = 'data.db'
# with open(filename, 'rb') as stream:
#     obj_restored = pickle.load(stream)
    
# print('obj_restored =', obj_restored)

### 🔴 Ćwiczenie

# Napisz program, który będzie bazował na pliku todos.db stworzonym w poprzednim ćwiczeniu.
# Załaduj plik do pamięci i wyświetl wszystkie zadania w formie tabeli.

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

@click.command()
def main():
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    
    print('=ID= DONE? ==DESC==')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f'{todo.id:4} {done:^5} {todo.description}')

if __name__ == "__main__":
    main()
