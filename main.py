import random

from crossover import partially_matched_crossover
from matrix import read_from_file, create_distances_matrix, create_cities
from mutation import swap_mutation
from population import create_population
from route import calc_route_length
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





# find fittest path called every generation
def find_fittest():
    key = 1000
    fittest = 0
    for i in range(population_size):
        if routes_length[i] < key:
            key = routes_length[i]
            fittest = i
    return fittest


# sorts parallely the lists
# def sort_alongside(routes_length, population):
#    routes_length, population = (list(i) for i in zip(*sorted(zip(routes_length, population))))


# initialize algorithm
create_population()
# print("Population initialization:", "\n", population)
calc_route_length()
# print("Population's paths length:", "\n", routes_length)

for j in range(n_generations):
    for i in range(0, population_size, 2):
        # pick parents for crossover
        parent1 = roulette_wheel_selection()
        parent2 = roulette_wheel_selection()
        # always pick different parents (not necessary)
        while True:
            if parent1 == parent2:
                parent2 = roulette_wheel_selection()
            else:
                break
        # update population
        population[i], population[i + 1] = partially_matched_crossover(population[parent1], population[parent2])
        # calculate lengths for updated generation
        calc_route_length()

    # pick the paths for mutation based on a probability
    for i in range(population_size):
        rand = random.uniform(0, 1)
        if rand < mutate_prob:
            swap_mutation(i)

    # calculate lengths after mutation
    calc_route_length()

    # find best path overall
    if routes_length[find_fittest()] < best_path:
        index = find_fittest()
        best_path = routes_length[index]

print("Best path is:", population[index], "with length", best_path)
