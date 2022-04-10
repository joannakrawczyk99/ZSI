from random import random

from main import cities, population_size, population, routes_length, fitness
from matrix import calc_distance

# creates a random route
def create_route():
    shuffled = random.sample(cities, len(cities))
    return shuffled


# calculates length of an route
def calc_route_length():
    for i in range(population_size):
        route_l = 0
        for j in range(1, len(cities)):
            route_l = route_l + calc_distance(population[i][j - 1], population[i][j])
        # route_l = route_l + calc_distance(population[i][len(cities)-1], population[i][1]) calculate distance from last to first
        routes_length[i] = route_l
        fitness[i] = 1 / routes_length[i]