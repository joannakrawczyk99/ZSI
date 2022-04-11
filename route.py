import random
from typing import List


def create_route(cities: List[List[int]]) -> List[List[int]]:
    shuffled = random.sample(cities, len(cities))
    return shuffled

