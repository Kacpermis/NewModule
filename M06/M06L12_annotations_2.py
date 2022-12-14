### 馃敶 Adnotacje list

# W poprzedniej lekcji dodawali艣my adnotacje typ贸w takich jak int, RenameOperation czy list.

# W tym ostatnim przypadku jednak tracimy informacj臋, jakiego typu s膮 elementy tej listy.

# Tym razem dodamy t膮 informacj臋.

# W tym celu skorzystamy z wbudowanego modu艂u typing, kt贸ry pozwala na bardziej zaawansowane adnotacje typ贸w:

from typing import List  # z du偶ej litery!

def print_all(strings: List[str]) -> None:  # tak, u偶ywamy List[str] - w nawiasach kwadratowych okre艣lamy typ element贸w listy
    for s in strings:
        print(s)
        
print_all(['a', 'b', 'c'])

# W Pythonie 3.8 i starszym musimy u偶y膰 typing.List zamiast list, poniewa偶 samo list nie pozwala jeszcze na zapis list[str].

# Jednak od Pythona 3.9 mo偶na ju偶 stosowa膰 zapis list[str].

### 馃敶 膯wiczenie

# Uzupe艂nij kod z 膰wiczenia M06L10 tak, aby u偶y膰 adnotacji typ贸w - zar贸wno prostych, jak i List.
import csv
from typing import List
TODOS_FILENAME = 'M06\\todos.csv'

class TodoItem:
    def __init__(self, id: int, description: str, done: bool) -> None:
        self.id = id
        self.description = description
        self.done = done

def read_toDo(filename):
    with open(filename) as stream:
        read = csv.DictReader(stream)
        todos = [ToDoItem_from_dict(row) for row in read]
    return todos

def ToDoItem_from_dict(row) -> TodoItem:
    return TodoItem(
        id=int(row['id']),
        description=row['desc'],
        done=(row['done'] == 'x'),
    )


def description(todos: List[TodoItem]) -> None:
    print("  ID  DONE? DESCRIPTION")
    print('---- ----- ------------')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f"{todo.id:6d} {done:^5} {todo.description}")
    
def summary(todos: List[TodoItem]) -> None:
    done = len([t for t in todos if t.done])
    all_ = len(todos)

    print()
    print(f"Number of fullfiled tasks: {done}/{all_}")

def main() -> None:
    todos = read_toDo(TODOS_FILENAME)
    description(todos)
    summary(todos)

if __name__ == "__main__":
    main()