### 🔴 Jak przyjemnie zmienia się kod, gdy jest dobrze napisany!

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu zmień zachowanie programu tak, że jeżeli baza danych nie istnieje, wówczas zamiast wyświetlać błąd automatycznie stwórz w pamięci nową, pustą bazę.import pickle
import pickle
import sys
from typing import List
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
    add_new(description, todos)
    save_db(todos)
    print('Dodano')

if __name__ == "__main__":
    cli()