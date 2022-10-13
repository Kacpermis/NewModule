### 🔴 pickle - najprostszy mechanizm perzystencji danych - zapis

# Często programy muszą przechowywać dane pomiędzy uruchomieniami.
# Dlatego przechowujemy dane w bazach danych albo prościej, w plikach CSV i innych formatach.
# Wymagają one jednak napisania kawałka kodu, który importuje i eksportuje takie dane.
# Moduł pickle pozwala Ci w bardzo prosty sposób zapisać dowolne obiekty do pliku - liczby, stringi, listy, słowniki, a nawet obiekty Twoich własnych klas.


# obj = [1, 2, 3]  # To może być dowolny obiekt, który chcesz zapisać.

# filename = 'data.db'  # rozszerzenie pliku nie ma znaczenia, tutaj użyliśmy .db
# with open(filename, 'wb') as stream:  # plik należy otworzyć w trybie BINARNYM zamiast tekstowym, stąd litera 'b'
#     pickle.dump(obj, stream)

### 🔴 Ćwiczenie

# Napisz program, który tworzy plik todos.db, w którym będzie przechowywana lista zadań.
# Po uruchomieniu tego programu lista zadań powinna być pusta, chyba że podano przełącznik --example - wówczas powinna zawierać przykładowe zadania (możesz zahardcodować je w kodzie).
import pickle

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
@click.option('--example', is_flag=True)
def main(example):
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


