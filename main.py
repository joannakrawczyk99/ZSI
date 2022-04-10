import csv
from typing import List

import random

from cities import create_cities
from crossover import partially_matched_crossover
from file import read_from_file
from matrix import create_distances_matrix
from mutation import swap_mutation
from selection import roulette_wheel_selection

population = []  # list that holds paths
population_size = 10  # max 120 combinations

mutate_prob = 0.1
n_generations = 4
routes_length = [0] * population_size
fitness = [0] * population_size
best_path = 1000

data = read_from_file('test.txt')

distances = create_distances_matrix(data)
print(distances)

cities = create_cities(data)
print(cities)


# calculates distance between 2 cities
def calc_distance(city1, city2):
    return distances[city1][city2]  # ord('A')=65


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


# creates starting population
def create_population():
    for i in range(population_size):
        population.append(create_route())


# find fittest path called every generation
def find_fittest():
    key = 1000
    fittest = 0
    for i in range(population_size):
        if routes_length[i] < key:
            key = routes_length[i]
            fittest = i
    return fittest


# initialize algorithm
create_population()
# print("Population initialization:", "\n", population)
calc_route_length()
# print("Population's paths length:", "\n", routes_length)

for j in range(n_generations):
    for i in range(0, population_size, 2):
        # pick parents for crossover
        parent1 = roulette_wheel_selection(population_size, fitness)
        parent2 = roulette_wheel_selection(population_size, fitness)
        # always pick different parents (not necessary)
        while True:
            if parent1 == parent2:
                parent2 = roulette_wheel_selection(population_size, fitness)
            else:
                break
        # update population
        population[i], population[i + 1] = partially_matched_crossover(population[parent1], population[parent2], cities)
        # calculate lengths for updated generation
        calc_route_length()

    # pick the paths for mutation based on a probability
    for i in range(population_size):
        rand = random.uniform(0, 1)
        if rand < mutate_prob:
            swap_mutation(i, cities, population)

    # calculate lengths after mutation
    calc_route_length()

    # find best path overall
    if routes_length[find_fittest()] < best_path:
        index = find_fittest()
        best_path = routes_length[index]

# wyświetl dane wyjściowe

pi = population[index]

for i in range(len(pi)):
    if i + 1 == len(pi):
        print(pi[i], ' ', end='')
    else:
        print(pi[i], '- ', end='')
print(best_path)
