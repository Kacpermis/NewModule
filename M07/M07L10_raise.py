### 🔴 Zgłaszanie błędów

# Do tej pory OBSŁUGIWALIŚMY błędy przy pomocy instrukcji try-except. Tym razem przyjrzymy się, jak my możemy ZGŁASZAĆ błędy.
# Robiliśmy to już w M04 przy pomocy sys.exit -- ale użycie tej funkcji powodowało natychmiastowe zakończenie programu, bez możliwości obsługi błędu.
# Tym razem poznasz instrukcję raise, która zgłasza błąd:

# raise ValueError("asdf")
# raise ValueError  # ✅ można bez nawiasów

# Taki błąd można normalnie obsłużyć instrukcją try-except:

description = ''
try:
    if description == "":
        raise ValueError("Opis nie może być pusty")
except ValueError:
    print("Nie można stworzyć zadania - pusty opis")

# Przy czym w praktyce najczęściej try-except znajduje się zupełnie gdzie indziej niż raise, inaczej moglibyśmy się ograniczyć do sprawdzania rezultatu if'em:

import csv

def validate_row(row):
    if 'id' not in row:
        raise ValueError("Missing id column")
    if row['id'] == '':
        raise ValueError('Missing id value')

def read_file():
    rows = []
    with open('M07/file.csv') as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            validate_row(row)
            rows.append(row)
    return rows

try:
    read_file()
except ValueError as e:
    print(f"Błąd: {e.args[0]}")


### 🔴 Ćwiczenie

# Rozwiń poprzednie ćwiczenie tak, aby nie można było stworzyć TodoItem z pustym opisem (description). W którym miejscu sprawdzisz, czy mamy niepusty opis? W którym miejscu złapiesz wyjątek?
import pickle
import sys
from typing import List
import click

DB_FILENAME = 'todos.db'

class TodoItem:
    def __init__(self, id, description, done):
        if not description:
            raise ValueError("description cannot be empyt")
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

def read_or_init():
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
    except FileNotFoundError:
        todos = []
    return todos

def save_db(todos, overwrite: bool = True):
    if overwrite:
        mode = 'wb'
    else:
        mode = 'xb'
    
    with open(DB_FILENAME, mode) as stream:
        pickle.dump(todos, stream)

def print_todos(todos):
    print(f'=ID= DONE? ==DESC==')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f'{todo.id:4} {done:^5} {todo.description}')

def add_new(description, todos):
    todo = TodoItem(
        id=next_id(todos),
        description=description,
        done=False
    )
    todos.append(todo)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--example', is_flag=True)
def init(example):
    todos: List[TodoItem]
    if example:
        todos = [
            TodoItem(id=1, description='Remember to make commits', done=False),
            TodoItem(id=2, description="Remember to make conventional commits", done=True),
            TodoItem(id=3, description="Task 3", done=False),
        ]
    else:
        todos = []
    
    try:
        with open(DB_FILENAME, 'xb') as stream:
            pickle.dump(todos,stream)
    except FileExistsError:
        print("File already exists")
    else:
        print("File created")

@cli.command()
def lsit():
    todos = read_or_init()
    print_todos(todos)

@cli.command()
@click.argument('description')
def add(description):
    todos = read_or_init()
    try:
        add_new(description, todos)
    except ValueError as e:
        print(f':Error {e.args[0]}')
        sys.exit(1)
    
    save_db(todos)
    print('Dodano')

if __name__ == "__main__":
    cli()
