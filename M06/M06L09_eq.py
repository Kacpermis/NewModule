### 馃敶 Programowanie obiektowe a testowanie

# Na ko艅cu ka偶dego testu zazwyczaj pojawi si臋 instrukcja assert got == expected.

# Je艣li por贸wnujemy inty, listy lub inne typy wbudowane, w贸wczas takie por贸wnanie dzia艂a tak, jak powinno.

# Jednak co w przypadku obiekt贸w naszych w艂asnych klas?

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
e1 = Expense(6.50, "Ziemniaki")
e2 = Expense(6.50, "Ziemniaki")
print(e1 == e2)  # ==> False

# Domy艣lnie ka偶dy wydatek jest traktowany jako nier贸wny innym - nawet, je艣li maj膮 ten sam opis i t膮 sam膮 kwot臋!

# Jak to zmieni膰? Kod `e1 == e2` jest zamieniany pod spodem na `e1.__eq__(e2)`. Wystarczy zatem zaimplementowa膰 metod臋 specjaln膮 __eq__:

# class Expense:
#     def __init__(self, amount, desc):
#         self.amount = amount
#         self.description = desc
        
#     def __eq__(self, other):
#         return self.amount == other.amount and self.description == other.description
        
# e1 = Expense(6.50, "Ziemniaki")
# e2 = Expense(6.50, "Ziemniaki")
print(e1 == e2)  # ==> True

### 馃敶 膯wiczenie

# W poprzednim 膰wiczeniu napisz testy funkcji collect_operation. B臋dzie to wymaga艂o zaimplementowania metody RenameOperation.__eq__.
from gc import collect
import os
import glob
EXTENSION = '.bak'

class RenameOperation:
    def __init__(self, old, new):
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

            


def ext_changing(filename):
    if '.' in filename:
        tokens = filename.rsplit('.', 1)
        name, extension = tokens   
    else:
        name = filename
        extension = ""
    return [name, extension]

def collect_operation(filename):
        name, extension = ext_changing(filename)
        new_filename = name + EXTENSION
        operation = RenameOperation(filename, new_filename)
        return operation

def show_change(operations):
    print("Zostana dokonane nastepujace zmiany: ")
    for op in operations:
        print(op)

def execute_change(operations):
    for op in operations:
        op.execute()
        print("Zmieniono", op.old, "--->", op.new)
        

def main():
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