### 馃敶 Programowanie obiektowe

# W module 4 przetwarzali艣my list臋 wydatk贸w - gdzie ka偶dy wydatek mia艂 pewn膮 kwot臋 oraz opis. Ka偶dy wydatek mo偶emy opisa膰 jako list臋:

expense = [6.50, "Ziemniaki"]

# Jednak ten spos贸b jest bardzo toporny - musimy pami臋ta膰, pod kt贸rym indexem jest cena i pod kt贸rym jest opis. Lepszym rozwi膮zaniem s膮 s艂owniki:

expense = {
    'amount': 6.50,
    'description': "Ziemniaki",
}

# Na s艂ownikach operuje si臋 du偶o lepiej. Gdyby艣my mieli przes艂a膰 nasze wydatki gdzie艣 w 艣wiat, to pewnie u偶yliby艣my s艂ownik贸w, skonwertowaliby艣my je na JSON i wys艂ali w 艣wiat.

# Jednak w samym programie jeszcze lepiej jest je przechowywa膰 jako obiekty W艁ASNEJ KLASY.

class Expense:
    def __init__(self, amount, desc):
        self.amount = amount
        self.description = desc
        
e = Expense(6.5, "Ziemniaki")  # to wywo艂uje metod臋 __init__() i tworzy nowy OBIEKT KLASY Expense 
# self jest automatycznie dodawany przez Pythona!

# Kilka rzeczy, o kt贸rych warto pami臋ta膰:

# 1. Funkcje w 艣rodku klasy to METODY.

# 2. Metody specjalne to metody zaczynaj膮ce si臋 i ko艅cz膮ce dwoma podkre艣leniami, np. __init__ albo __repr__.

# 3. Najwa偶niejsz膮 metod膮 specjaln膮 jest __init__, kt贸ry jest wywo艂ywany gdy tworzysz nowy obiekt.

# 4. Przy wywo艂ywaniu metod obowi膮zuj膮 te same zasady co przy wywo艂ywaniu funkcji, czyli argumenty mo偶na przekazywa膰 w spos贸b zar贸wno pozycyjny, jak i nazwany:

e = Expense(6.5, desc="Ziemniaki")

# 5. Nie musimy zawczasu okre艣la膰, jakie POLA b臋d膮 mie膰 obiekty - po prostu tworzymy je DYNAMICZNIE w __init__.

# Teraz mo偶emy korzysta膰 z takiego obiektu:

print('e.amount =', e.amount)
print('e.description =', e.description)

### 馃敶 膯wiczenie

# Popraw kod z 膰wiczenia M03L16. W tym 膰wiczeniu zmieniali艣my rozszerzenia wielu plik贸w na raz. 

# Po pierwsze, zastosuj nowe dobre praktyki, kt贸re pozna艂忙艣 w czwartym i pi膮tym module.

# Po drugie, w tym programie tworzyli艣my list臋 wszystkich operacji do wykonania. Ka偶d膮 operacj臋 reprezentowali艣my jako dwuelementowa lista [obecna_nazwa_pliku, nowa_nazwa_pliku].

# Du偶o lepiej jest reprezentowa膰 operacj臋 jako obiekt w艂asnej klasy RenameOperation.

# Stw贸rz tak膮 klas臋 i przepisz kod tak, aby j膮 wykorzystywa艂.
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
        print(op.old, "--->", op.new)

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