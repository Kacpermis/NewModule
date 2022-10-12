### 🔴 Podpolecenia z click

# W poprzednich trzech lekcjach napisałæś trzy programy pozwalające na zarządzanie listą zadań. Wszystkie trzy sporo łączy.
# Najczęściej takie skrypty łączy się w jeden, rozróżniając między nimi dzięki podpoleceniu:

# $ python todos.py init --example
# $ python todos.py list
# $ python todos.py add "Nowe zadanie"

# Biblioteka click pozwala na automatyczne rozróżnianie między różnymi podpoleceniami, tak aby na końcu została wywołana odpowiednia funkcja. W tym celu tworzymy grupę:

# import click

# @click.group()
# def cli():
#     pass  # Instrukcja pass nie robi nic, ale jest konieczna, ponieważ każdy blok kodu musi mieć conajmniej jedną instrukcję, inaczej mamy SyntaxError

# # A następnie rejestrujemy kilka funkcji w tej grupie:

# @cli.command()  # `cli` zamiast `click`!
# def happy():
#     print(':-)')
    
# @cli.command()
# def sad():
#     print(':-(')

# @cli.command()
# @click.argument('msg')  # A tutaj już normalnie `click` zamiast `cli`
# def custom(msg):
#     print(f':-| {msg}')

# if __name__ == "__main__":
#     cli()

# Teraz ten program możemy wywołać na kilka sposobów:

# $ python M07/M07L08_subcommands.py happy
# $ python M07/M07L08_subcommands.py sad
# $ python M07/M07L08_subcommands.py custom "Custom text"

### 🔴 Ćwiczenie

# W poprzednich ćwiczeniach napisałæś trzy programy do zarządzania listą zadań umieszczoną w pliku todos.db. Połącz te trzy programy w jeden skrypt, tak aby miał podpolecenia init, list i add.
# Jak podzielisz cały kod na funkcje? Co będzie robiła każda z funkcji?
# Napisz testy! Które funkcje przetestujesz?
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

def read_or_exit():
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    return todos

def save_db(todos, overwrite):
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
    todos = read_or_exit()
    print_todos(todos)

@cli.command()
@click.argument('description')
def add(description):
    todos = read_or_exit()
    add_new(description, todos)
    save_db(todos)
    print('Dodano')

if __name__ == "__main__":
    cli()