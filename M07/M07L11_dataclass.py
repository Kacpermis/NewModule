### 🔴 dataclass'y - szybki sposób na tworzenie klas

# Często Twoje klasy wymagają metod takich jak:

# - __init__
# - __repr__ (dla łatwiejszego debugowania)
# - __eq__ (dla testów)

# Ale te metody są bardzo schematyczne:

# class Expense:
#     def __init__(self, amount: int, description: str):
#         self.amount = amount
#         self.description = description
#         print(f'Sukces! {self.amount}')
        
#     def __eq__(self, other):
#         return self.amount == other.amount and self.description == other.description
    
#     def __repr__(self):
#         return f"Expense(amount={self.amount!r}, description={self.description!r})"

# e = Expense(2.5, 'Ziemniaki')
# e2 = Expense(2.5, 'Ziemniaki')
# print(e)
# print(e == e2)
    
# # Dlatego wymyślono mechanizm dataclass, który powoduje automatyczne wygenerowanie m.in. tych trzech metod. Wystarczy tylko określić jakie pola będzie mieć klasa:

# from dataclasses import dataclass

# @dataclass
# class Expense:
#     amount: int
#     description: str
        
#     # Jeśli jest potrzeba wykonania czegoś nietypowego w __init__, wówczas piszemy __post_init__ zamiast __init__:
#     def __post_init__(self):
#         print(f'Sukces! {self.amount}')
        
# e = Expense(2.5, 'Ziemniaki')
# e2 = Expense(2.5, 'Ziemniaki')
# print(e)
# print(e == e2)

### 🔴 Ćwiczenie

# Przepisz kod z poprzedniego ćwiczenia tak, aby klasę TodoItem zaimplementować jako dataclass.

import pickle
import sys

from typing import List
from dataclasses import dataclass
import click

DB_FILENAME = 'todos.db'

@dataclass
class TodoItem:
    id: int
    description: str
    id: bool

    def __post_init__(self):
        if self.description == "":
            raise ValueError("description cannot be empty")

   
        


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
    print('=ID= DONE? ==DESC==')
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