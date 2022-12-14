### 馃敶 pickle - najprostszy mechanizm perzystencji danych - zapis

# Cz臋sto programy musz膮 przechowywa膰 dane pomi臋dzy uruchomieniami.
# Dlatego przechowujemy dane w bazach danych albo pro艣ciej, w plikach CSV i innych formatach.
# Wymagaj膮 one jednak napisania kawa艂ka kodu, kt贸ry importuje i eksportuje takie dane.
# Modu艂 pickle pozwala Ci w bardzo prosty spos贸b zapisa膰 dowolne obiekty do pliku - liczby, stringi, listy, s艂owniki, a nawet obiekty Twoich w艂asnych klas.


# obj = [1, 2, 3]  # To mo偶e by膰 dowolny obiekt, kt贸ry chcesz zapisa膰.

# filename = 'data.db'  # rozszerzenie pliku nie ma znaczenia, tutaj u偶yli艣my .db
# with open(filename, 'wb') as stream:  # plik nale偶y otworzy膰 w trybie BINARNYM zamiast tekstowym, st膮d litera 'b'
#     pickle.dump(obj, stream)

### 馃敶 膯wiczenie

# Napisz program, kt贸ry tworzy plik todos.db, w kt贸rym b臋dzie przechowywana lista zada艅.
# Po uruchomieniu tego programu lista zada艅 powinna by膰 pusta, chyba 偶e podano prze艂膮cznik --example - w贸wczas powinna zawiera膰 przyk艂adowe zadania (mo偶esz zahardcodowa膰 je w kodzie).
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


