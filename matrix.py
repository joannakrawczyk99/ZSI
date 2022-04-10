import csv
from typing import List

from main import distances


def read_from_file(path: str, delimiter=" "):
    with open(path, newline="") as file:
        return [line for line in csv.reader(file, delimiter=delimiter)]

def create_distances_matrix(data: List[List[int]]):
    size = int(data[0][0])
    matrix = [[None] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            try:
                matrix[x][y] = int(data[x + 1][y])
            except IndexError:
                matrix[x][y] = int(data[y + 1][x])
    return matrix

def create_cities(distances: List[List[int]]) -> List[int]:
    size = int(distances[0][0])
    print(size)
    cities = []
    for i in range(size):
        cities.append(i)
        i + 1
    return cities

# calculates distance between 2 cities
def calc_distance(city1, city2):
    return distances[city1][city2]  # ord('A')=65
