### 馃敶 Jeszcze wi臋cej wyra偶e艅 listowych

# Do realizacji kolejnego 膰wiczenia potrzebujesz wbudowanej funkcji sum():

numbers = [2, 3, 4]
sum_ = sum(numbers)
print('sum_ =', sum_)  # ==> sum_ = 9

# Ta funkcja jest przydatna, kiedy zliczamy pewne elementy. Nie musimy wtedy tworzy膰 licznika `total`, tak jak poni偶ej:

total = 0
for n in numbers:
    total += n
print('total =', total)

### 馃敶 膯wiczenie

# Popraw program M01L13. W tym programie sprawdzali艣my z艂o偶ono艣膰 tekst贸w licz膮c jaka jest 艣rednia d艂ugo艣膰 s艂贸w. Na tamtym etapie nie znali艣my metody jak wyliczy膰 t膮 wielko艣膰 dok艂adnie, bez spacji, znak贸w interpunkcyjnych czy te偶 pomijaj膮c liczby w tek艣cie.

# Popraw kod tak, aby nie zlicza艂 spacji ani znak贸w interpunkcyjnych. Dodatkowo, je艣li w tek艣cie pojawiaj膮 si臋 liczby, to r贸wnie偶 nie bierz ich pod uwag臋.

# Napisz testy!

PUNCTUACTION = '.,!?'


def remove_punctuaction(text):
    for punc in PUNCTUACTION:
        text = text.replace(punc, ' ')
    return text

def compute_average_length(text):
    words = remove_punctuaction(text).split()
    without_numbers = [w for w in words if not w.isnumeric()]
    lenghts = [len(w) for w in without_numbers]
    average = sum(lenghts) / len(lenghts)

def main():
    text = input('Podaj tekst: ')
    average = compute_average_length(text)
    print(f'Average length of a word: {average:.2f}')

if __name__ == '__main__':
    main()




    

