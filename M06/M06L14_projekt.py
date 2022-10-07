# Napisz własną analitykę do aplikacji do śledzenia czasu takich jak np. Toggl Track. Twój moduł wczytuje dane o czasie wykonania poszczególnych zadań w formacie CSV, a następnie generuje raport wykorzystania czasu z podziałem na projekty, klientów i inne tagi.

# 1. Dane w pliku CSV mają trzy kolumny: desc, time oraz tags. Desc jest opisem zadania. Time to liczba całkowita określająca czas wykonywania tego zadania w minutach. Natomiast tags jest listą tagów porozdzielanych spacjami. Jedno zadanie może mieć wiele tagów. Jednym tagiem może być otagowane wiele zadań. Tagi służą do oznaczania zadań wg projektów, klientów lub innych kryteriów.

# 2. Upakuj te trzy informacje w klasie Entry. Upewnij się, że ma ona metodę __repr__.

# 3. Program przyjmuje scieżkę do pliku CSV jako argument linii poleceń. Następnie wyświetla raport. Każda jego linia to jeden tag. Dla każdego tagu wyliczona jest suma wszystkich otagowanych nim zadań.

# 4. Nie musisz pisać testów, ale podziel program na funkcje tak, aby każda z nich robiła tylko jedną rzecz.
import csv
from typing import Dict, List
import sys
FILENAME = sys.argv[1]

class timeTrack:
    def __init__(self, desc: str, time: int, tag: str):
        self.desc = desc
        self.time = time
        self.tag = tag

def file_reader():
    with open(FILENAME) as stream:
        read = csv.DictReader(stream)
        sorted = [timeTrack_dict(row) for row in read]
    print(sorted)
    return sorted

def timeTrack_dict(row: Dict[str, str]) -> timeTrack:
    return timeTrack(
        desc=row['desc'],
        time=int(row['time']),
        tag=row['tags'],
    )

def main():
    file_reader()

if __name__ == "__main__":
    main()
