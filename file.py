import csv


def read_data(path, delimiter=" "):
    with open(path, newline="") as file:
        return [line for line in csv.reader(file, delimiter=delimiter)]
