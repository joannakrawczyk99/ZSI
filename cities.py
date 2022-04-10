from typing import List


def create_cities(distances: List[List[int]]) -> List[int]:
    size = int(distances[0][0])
    print(size)
    cities = []
    for i in range(size):
        cities.append(i)
        i + 1
    return cities