### 🔴 Metody we własnych klasach

# W poprzedniej lekcji napisaliśmy najprostszą klasę, taką która ma tylko metodę specjalną __init__.

# Teraz pora dodać nową, zwykłą metodę.

# Czegoś takiego nie moglibyśmy zrobić, gdybyśmy reprezentowali wydatek jako słownik. Dzięki zdefiniowaniu własnej klasy jest to jednak możliwe.

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
    def get_amount_as_int(self):
        ''' Return amount in GROSZE as int.  '''
        return int(self.amount * 100)
    
e = Expense(6.50, "Ziemniaki")

print('e.amount =', e.amount)

# Zwróć uwage, że wywołując metodę nie podajesz self'a w nawias okrągłych - bo jego podajesz przed kropką.
grosze = e.get_amount_as_int()

print('Ziemniaki kosztowały', grosze, 'groszy.')

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu zaimplementuj metodę RenameOperation.display(), która wyświetla operację, jaka zostanie wykonana. Wykorzystaj tę metodę w reszcie kodu.

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
        RenameOperation.display()

def execute_change(operations):
    for op in operations:
            os.rename(op.old, op.new)
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