### 🔴 Adnotacje Dict

# W poprzedniej lekcji poznałæś tzw. typ parametryczny, jakim jest List[X].

# Podobnie jest ze słownikami - dobrze będzie określić, jakiego typu są klucze i jakiego typu są wartości. W tym celu używamy Dict[Key, Value]:

from typing import Dict, List

def count_words(words: List[str]) -> Dict[str, int]:
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter

print(count_words(['a', 'b', 'c', 'a']))

# Jeśli jednak słownik reprezentuje pewien obiekt, wówczas klucze są stringami, ale wartości mogą być różnego typu, np.:

expense = {
    'amount': 6.50,
    'description': "Ziemniaki",
}

# Jak opisać taki słownik? Użyjemy typing.Any, który oznacza dowolny typ.

from typing import Any

def process_expense(expense: Dict[str, Any]):
    print(expense)

### 🔴 Ćwiczenie

# Uzupełnij kod z poprzedniego ćwiczenia tak, aby uzupełnić brakujące adnotacje typów dotyczące samego słownika.
import csv
from typing import Dict, List
TODOS_FILENAME = 'M06\\todos.csv'

class TodoItem:
    def __init__(self, id: int, description: str, done: bool) -> None:
        self.id = id
        self.description = description
        self.done = done

def read_toDo(filename: str) -> List[TodoItem]:
    with open(filename) as stream:
        read = csv.DictReader(stream)
        todos = [ToDoItem_from_dict(row) for row in read]
    return todos

def ToDoItem_from_dict(row: Dict[str, str]) -> TodoItem:
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