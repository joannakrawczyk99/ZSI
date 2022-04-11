import random
from typing import List


def mutation(ind: int, cities: List[List[int]], population: List[List[int]]):
    picks = random.sample(range(len(cities)), 2)
    temp = population[ind][picks[0]]
    population[ind][picks[0]] = population[ind][picks[1]]
    population[ind][picks[1]] = temp
