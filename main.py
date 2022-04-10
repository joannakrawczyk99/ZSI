import random

from cities import create_cities
from crossover import crossover
from file import read_data
from matrix import create_matrix
from mutation import mutation
from route import create_route
from selection import selection

population = []  # list that holds paths
population_size = 20  # max 120 combinations
mutate_prob = 0.2
n_generations = 5
routes_length = [0] * population_size
fitness = [0] * population_size
best_path = 1000
data = read_data('a280.txt')
distances = create_matrix(data)


def calc_distance(city1, city2):
    return distances[city1][city2]


cities = create_cities(data)


def calc_route_length():
    for i in range(population_size):
        route_l = 0
        for j in range(1, len(cities)):
            route_l = route_l + calc_distance(population[i][j - 1], population[i][j])
        routes_length[i] = route_l
        fitness[i] = 1 / routes_length[i]


def create_population():
    for i in range(population_size):
        population.append(create_route(cities))


def find_fittest():
    key = 1000
    fittest = 0
    for i in range(population_size):
        if routes_length[i] < key:
            key = routes_length[i]
            fittest = i
    return fittest


create_population()
calc_route_length()

for j in range(n_generations):
    for i in range(0, population_size, 2):
        parent1 = selection(population_size, fitness)
        parent2 = selection(population_size, fitness)
        while True:
            if parent1 == parent2:
                parent2 = selection(population_size, fitness)
            else:
                break
        population[i], population[i + 1] = crossover(population[parent1], population[parent2], cities)
        calc_route_length()

    for i in range(population_size):
        rand = random.uniform(0, 1)
        if rand < mutate_prob:
            mutation(i, cities, population)

    calc_route_length()

    index = find_fittest()
    best_path = routes_length[index]


pi = population[index]

for i in range(len(pi)):
    if i + 1 == len(pi):
        print(pi[i], ' ', end='')
    else:
        print(pi[i], '- ', end='')
print(best_path)
