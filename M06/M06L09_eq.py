### 🔴 Programowanie obiektowe a testowanie

# Na końcu każdego testu zazwyczaj pojawi się instrukcja assert got == expected.

# Jeśli porównujemy inty, listy lub inne typy wbudowane, wówczas takie porównanie działa tak, jak powinno.

# Jednak co w przypadku obiektów naszych własnych klas?

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
e1 = Expense(6.50, "Ziemniaki")
e2 = Expense(6.50, "Ziemniaki")
print(e1 == e2)  # ==> False

# Domyślnie każdy wydatek jest traktowany jako nierówny innym - nawet, jeśli mają ten sam opis i tą samą kwotę!

# Jak to zmienić? Kod `e1 == e2` jest zamieniany pod spodem na `e1.__eq__(e2)`. Wystarczy zatem zaimplementować metodę specjalną __eq__:

# class Expense:
#     def __init__(self, amount, desc):
#         self.amount = amount
#         self.description = desc
        
#     def __eq__(self, other):
#         return self.amount == other.amount and self.description == other.description
        
# e1 = Expense(6.50, "Ziemniaki")
# e2 = Expense(6.50, "Ziemniaki")
print(e1 == e2)  # ==> True

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu napisz testy funkcji collect_operation. Będzie to wymagało zaimplementowania metody RenameOperation.__eq__.
import os
import glob


pattern = input('Podaj pattern: ')
ext = '.bak'
files = glob.glob(pattern)
operations = []

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

            


def ext_changing():
    for x in files:
        if '.' in x:
            name = x.rsplit('.', 1)
            nazwa, extension = name   
        else:
            name = x
            extension = ""
        new_filename = nazwa + ext
        operation = RenameOperation(x, new_filename)
        operations.append(operation)

def show_change(operations):
    print("Zostana dokonane nastepujace zmiany: ")
    for op in operations:
        print(op)

def execute_change(operations):
    for op in operations:
        op.execute()
        print("Zmieniono", op.old, "--->", op.new)
        

def main():
    ext_changing()
    show_change(operations)
    zgoda = input('Kontynuowac? [t/n]')
    if zgoda.lower() == 't':
        execute_change(operations)
    else:
        print('Anulowano')

if __name__ == "__main__":
    main()