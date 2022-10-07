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
        self.tags = tag
    
    def __repr__(self):
        return f"timeTrack(desc={self.desc!r}, time={self.time!r}, tags={self.tag!r})"
    
    def __str__(self):
        tags = [f'#{t}' for t in self.tags]
        tags = " ".join(tags)
        return f"{self.desc} ({self.time} min) {tags}"

def file_reader():
    with open(FILENAME) as stream:
        read = csv.DictReader(stream)
        sorted = [timeTrack_dict(row) for row in read]
    return sorted

def timeTrack_dict(row: Dict[str, str]) -> timeTrack:
    tags = row['tags'].split(' ')
    tags = [tag.strip() for tag in tags]
    entry = timeTrack(
        desc=row['desc'].strip(),
        time=int(['time'].strip()),
        tags=tags,
    )
    return timeTrack


    


def time_of_tags(entries):
    tags = {t for e in entries for t in e.tags}
    report = {}
    for tag in tags:
        total = sum([e.time for e in entries if tag in e.tags])
        report[tag] = total
    return report

# def description(sorted: List[timeTrack]) -> None:
#     print("TOTAL-TIME  TAG")
#     for sort in sorted:
    
