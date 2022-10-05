### 🔴 Wincyj metod!

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu dodaj metodę RenameOperation.execute(), która dokonuje faktycznej zmiany nazwy pliku, czyli wywołuje funkcję os.rename. Przepisz resztę kodu tak, aby wykorzystywała tę metodę.

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

    def display(self):
        print(self.old, "-->", self.new)

    def execute(self):
            os.rename(self.old, self.new)
            


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
        op.display()

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