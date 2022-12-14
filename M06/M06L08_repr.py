### 馃敶 Metody specjalne __repr__ i __str__

### 馃敶 Metoda __str__

# Wywo艂anie print'a wywo艂uje pod spodem metod臋 specjaln膮 __str__. Dzi臋ki temu print dzia艂a z obiektem dowolnego typu, niezale偶nie czy jest to int, list czy Twoja w艂asna klasa RenameOperation.

number = 2
print('number =', number)
print('number.__str__() =', number.__str__())

text = "asdf"
print('text =', text)
print('text.__str__() =', text.__str__())

# Wystarczy wi臋c zaimplementowa膰 metod臋 __str__, aby okre艣li膰, jak maj膮 by膰 printowane obiekty Twoich klas:

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
    def __str__(self):
        return f"wydatek w kwocie {self.amount} na {self.description}"

e = Expense(6.50, "Ziemniaki")
print('e =', e)
print('e.__str__() =', e.__str__())

# Co ciekawe, nawet jak nie zdefiniujesz metody __str__, w贸wczas Python i tak doda tak膮 metod臋 do Twojej klasy:

class DummyExpense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc

de = DummyExpense(6.50, "Ziemniaki")
print('de =', de)
print('de.__str__() =', de.__str__())
      
### 馃敶 Metoda __repr__    
    
# Opr贸cz metody __str__() mamy jeszcze drug膮 metod臋 specjaln膮 __repr__(), kt贸ra r贸wnie偶 konwertuje obiekt na napis.

# __str__ powinien zwr贸ci膰 wersj臋 "dla cz艂owieka", natomiast __repr__ najlepiej, aby zwr贸ci艂 kod, kt贸ry nam wygeneruje ten obiekt z powrotem.

# W przypadk贸w liczb rezultat jest taki sam:

number = 10
print(number, number.__str__(), number.__repr__())

# Ale ju偶 w przypadku string贸w wida膰 r贸偶nic臋:
text = "asdf"
print(text, text.__str__(), text.__repr__())

# W print oraz w string interpolation domy艣lnie u偶ywana jest metoda __str__. Je艣li jednak chcemy, mo偶emy u偶y膰 __repr__:

msg = f"text = {text!r}"
print(msg)

# Zobaczmy jak mo偶emy doda膰 metod臋 __repr__ w naszych w艂asnych klasach

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
    def __str__(self):
        return f"wydatek w kwocie {self.amount} na {self.description}"

    def __repr__(self):
        return f"Expense({self.amount!r}, {self.description!r})"  # konieczne !r, aby Python sam otoczy艂 string cudzys艂owami!
    
    
e = Expense(6.50, "Ziemniaki")
print('e =', e)
print('e.__str__() =', e.__str__())
print('e.__repr__() =', e.__repr__())

# Warto jeszcze zwr贸ci膰 uwag臋, 偶e kiedy printujemy list臋, to uruchamiana jest jej metoda __str__. Jednak dla ka偶dego jej elementu wywo艂uje ju偶 metod臋 __repr__:

list_ = [1, "asdf", e]
print('list_ =', list_)

### 馃敶 Funkcje str() i repr()

# Praktycznie nigdy nie wywo艂ujemy bezpo艣rednio metod __str__() i __repr__. Zamiast tego wywo艂ujemy funkcje str() i repr(), kt贸re dopiero deleguj膮 do odpowiednich metod.

print('e =', e)
print('str(e) =', str(e))
print('repr(e) =', repr(e))

### 馃敶 膯wiczenie

# W poprzednim 膰wiczeniu zaimplementuj metod臋 __repr__ oraz __str__ w klasie RenameOperation i wykorzystaj j膮 w reszcie kodu. 

# Zauwa偶, 偶e nie b臋dziemy ju偶 potrzebowali metody display().

# Je艣li nie wywo艂ujesz nigdzie metody __repr__, to czy jest sens j膮 implementowa膰?
### 馃敶 Wincyj metod!

### 馃敶 膯wiczenie

# W poprzednim 膰wiczeniu dodaj metod臋 RenameOperation.execute(), kt贸ra dokonuje faktycznej zmiany nazwy pliku, czyli wywo艂uje funkcj臋 os.rename. Przepisz reszt臋 kodu tak, aby wykorzystywa艂a t臋 metod臋.

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