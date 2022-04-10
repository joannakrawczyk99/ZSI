# swap with a probability 2 cities in a route
from random import random

from main import cities, population


def swap_mutation(ind):
    picks = random.sample(range(len(cities)), 2)
    temp = population[ind][picks[0]]
    population[ind][picks[0]] = population[ind][picks[1]]
    population[ind][picks[1]] = temp
    # print("Mutated path: ", population[ind])