### 🔴 Adnotacje typów

# Wiesz już, że warto umieszczać w kodzie dokumentację w postaci docstringów.

# Można tam umieścić także informacje o typie poszczególnych parametrów jak i wartości zwracanej.

# Jest jednak na to lepszy sposób, dzięki któremu VSCode i inne IDE będą potrafiły wykorzystać tą informację, aby lepiej podpowiadać. Łatwiej będzie ją też znaleźć ludziom.

# Są to adnotacje typów parametrów oraz wartości zwracanej. Można ich używać w sygnaturach funkcji, jak i metod (także metod specjalnych).

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 4))
print(add('asdf', 'qwer'))  # Zwróć uwagę, że adnotacje typów to jedynie adnotacje. Python nie sprawdza, czy faktycznie ma do czynienia z właściwym typem - ani na etapie kompilacji, ani w runtimie.

### 🔴 Ćwiczenie

# Dodaj adnotacje typów w M06L09.

from gc import collect
import os
import glob
EXTENSION = '.bak'

class RenameOperation:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new

    def execute(self):
            os.rename(self.old, self.new)

    def __str__(self):
        return f"{self.old} -> {self.new}"
    
    def _repr__(self):
        return f"RenameOperation(old={self.old!r}, new={self.new!r}"

    def __eq__(self, other):
        return self.old == other.old and self.new == other.new

            


def ext_changing(filename: str) -> list:
    if '.' in filename:
        tokens = filename.rsplit('.', 1)
        name, extension = tokens   
    else:
        name = filename
        extension = ""
    return [name, extension]

def collect_operation(filename: str) -> RenameOperation:
        name, extension = ext_changing(filename)
        new_filename = name + EXTENSION
        operation = RenameOperation(filename, new_filename)
        return operation

def show_change(operations: list) -> None:
    print("Zostana dokonane nastepujace zmiany: ")
    for op in operations:
        print(op)

def execute_change(operations) -> None:
    for op in operations:
        op.execute()
        print("Zmieniono", op.old, "--->", op.new)
        

def main() -> None:
    pattern = input('Podaj pattern: ')
    filenames = glob.glob(pattern)
    operations = [collect_operation(filename) for filename in filenames]

    show_change(operations)
    zgoda = input('Kontynuowac? [t/n]')
    if zgoda.lower() == 't':
        execute_change(operations)
    else:
        print('Anulowano')

if __name__ == "__main__":
    main()