import random

from cities import create_cities
from crossover import crossover
from file import read_data, prepare_data
from matrix import create_matrix
from mutation import mutation
from parameters import population_size, path_holder, routes_length, fitness, n_generations, mutate_prob
from route import create_route
from selection import selection

prepare_data('test2.txt')
data = read_data('test2.txt')
distances = create_matrix(data)


def calc_distance(city1, city2):
    return distances[city1][city2]


cities = create_cities(data)


def calc_route_length():
    for i in range(population_size):
        route_l = 0
        for j in range(1, len(cities)):
            route_l = route_l + calc_distance(path_holder[i][j - 1], path_holder[i][j])
        routes_length[i] = route_l
        fitness[i] = 1 / routes_length[i]


def create_population():
    for i in range(population_size):
        path_holder.append(create_route(cities))


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
        path_holder[i], path_holder[i + 1] = crossover(path_holder[parent1], path_holder[parent2], cities)
        calc_route_length()

    for i in range(population_size):
        rand = random.uniform(0, 1)
        if rand < mutate_prob:
            mutation(i, cities, path_holder)

    calc_route_length()

    index = find_fittest()
    best_path = routes_length[index]

pi = path_holder[index]

for i in range(len(pi)):
    if i + 1 == len(pi):
        print(pi[i], ' ', end='')
    else:
        print(pi[i], '- ', end='')
print(best_path)
