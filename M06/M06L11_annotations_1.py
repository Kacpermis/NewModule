### 馃敶 Adnotacje typ贸w

# Wiesz ju偶, 偶e warto umieszcza膰 w kodzie dokumentacj臋 w postaci docstring贸w.

# Mo偶na tam umie艣ci膰 tak偶e informacje o typie poszczeg贸lnych parametr贸w jak i warto艣ci zwracanej.

# Jest jednak na to lepszy spos贸b, dzi臋ki kt贸remu VSCode i inne IDE b臋d膮 potrafi艂y wykorzysta膰 t膮 informacj臋, aby lepiej podpowiada膰. 艁atwiej b臋dzie j膮 te偶 znale藕膰 ludziom.

# S膮 to adnotacje typ贸w parametr贸w oraz warto艣ci zwracanej. Mo偶na ich u偶ywa膰 w sygnaturach funkcji, jak i metod (tak偶e metod specjalnych).

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 4))
print(add('asdf', 'qwer'))  # Zwr贸膰 uwag臋, 偶e adnotacje typ贸w to jedynie adnotacje. Python nie sprawdza, czy faktycznie ma do czynienia z w艂a艣ciwym typem - ani na etapie kompilacji, ani w runtimie.

### 馃敶 膯wiczenie

# Dodaj adnotacje typ贸w w M06L09.

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