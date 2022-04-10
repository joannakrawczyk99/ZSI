import csv


def read_from_file(path: str, delimiter=" "):
    with open(path, newline="") as file:
        return [line for line in csv.reader(file, delimiter=delimiter)]