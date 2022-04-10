# swap with a probability 2 cities in a route
import random


def mutation(ind, cities, population):
    picks = random.sample(range(len(cities)), 2)
    temp = population[ind][picks[0]]
    population[ind][picks[0]] = population[ind][picks[1]]
    population[ind][picks[1]] = temp
    # print("Mutated path: ", population[ind])
