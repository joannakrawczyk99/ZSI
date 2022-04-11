from typing import List


def create_cities(distances: List[List[int]]) -> List[List[int]]:
    size = int(distances[0][0])
    cities = []
    for i in range(size):
        cities.append(i)
        i + 1
    return cities

