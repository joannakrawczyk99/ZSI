import csv

def prepare_data(path):
    with open(path) as file:
        for line in file:
            line.rstrip()


def read_data(path, delimiter=" "):
    with open(path, newline="") as file:
        return [line for line in csv.reader(file, delimiter=delimiter)]
