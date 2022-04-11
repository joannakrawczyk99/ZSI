import csv
from typing import List

def prepare_data(path: str):
    with open(path) as file:
        for line in file:
            line.rstrip()


def read_data(path: str, delimiter=" ") -> List[List[int]]:
    with open(path, newline="") as file:
        return [line for line in csv.reader(file, delimiter=delimiter)]
