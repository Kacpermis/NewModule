### 馃敶 Instrukcja break

# Funkcja eval
# result = eval('2+2')
# print('result =', result)
# print('type(result) =', type(result))

# # Przyk艂adowy REPL - Read-Eval-Print Loop.
# while True:
#     expr = input('>>> ')
#     if expr.lower().strip() == 'exit':
#         break  # Instrukcja break natychmiast przerywa wykonywanie p臋tli i przenosi nas za p臋tle do 'Finish'
#     result = eval(expr)
#     print(result)
# print('Finish')

### 馃敶 膯wiczenie

# Pracujesz dla Google i jeste艣 odpowiedzialny za rozw贸j przegl膮darki Google Chrome.
# Twoim zadaniem jest napisa膰 modu艂 odpowiedzialny za pobieranie plik贸w.
# W momencie pobierania pliku "plik.txt" zapisujesz go na dysku dok艂adnie pod t膮 sam膮 nazw膮, CHYBA 呕E ju偶 taki plik istnieje.
# W takiej sytuacji nie chcesz go nadpisa膰, dlatego zapisujesz plik pod nazw膮 "plik-2.txt".
# Je艣li ta nazwa r贸wnie偶 jest ju偶 zaj臋ta, to zapisz do pliku "plik-3.txt" itd.
# Twoim zadaniem jest napisa膰 funkcj臋, kt贸ra otrzymuje nazw臋 pliku i zwraca t膮 nazw臋 z doklejon膮 odpowiedni膮 ko艅c贸wk膮 "-2", "-3" itd., tak 偶eby nie nadpisa膰 偶adnego pliku.
# Jakiej funkcji u偶yjesz do sprawdzenia, czy plik ju偶 istnieje?
# Napisz testy! W jaki spos贸b przetestujesz sw贸j kod?

from os.path import exists
from typing import Tuple, Optional

def split_name(filename: str) -> Tuple[str, Optional[str]]:
    if '.' in filename:
        name, ext = filename.rsplit('.', maxsplit=1)
    else: 
        name, ext = filename, None
    return name, ext

def construct_filename(name: str, counter: int, ext: Optional[str]) -> str:
    if ext is None:
        ext_part = ''
    else:
        ext_part = '.' + ext
    return f'{name}-{counter}{ext_part}'

def generate_name(filename: str) -> str:
    if exists(filename):
        name, ext = split_name(filename)
        counter = 2

        while True:
            new_filename = construct_filename(name, counter, ext)
            if not exists(new_filename):
                break
            counter += 1
        return new_filename
    else: 
        return filename
