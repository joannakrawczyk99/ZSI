import csv
from typing import List

import random

population = []  # list that holds paths
population_size = 10  # max 120 combinations
mutate_prob = 0.1
n_generations = 4
routes_length = [0] * population_size
fitness = [0] * population_size
best_path = 1000


def read_from_file(path: str, delimiter=" "):
    with open(path, newline="") as file:
        return [line for line in csv.reader(file, delimiter=delimiter)]


data = read_from_file('test.txt')



def create_distances_matrix(data: List[List[int]]):
    size = int(data[0][0])
    matrix = [[None] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            try:
                matrix[x][y] = int(data[x + 1][y])
            except IndexError:
                matrix[x][y] = int(data[y + 1][x])
    return matrix


distances = create_distances_matrix(data)
print(distances)

def create_cities(distances: List[List[int]]) -> List[int]:
    size = int(distances[0][0])
    print(size)
    cities = []
    for i in range(size):
        cities.append(i)
        i + 1
    return cities


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


# swap with a probability 2 cities in a route
def swap_mutation(ind):
    picks = random.sample(range(len(cities)), 2)
    temp = population[ind][picks[0]]
    population[ind][picks[0]] = population[ind][picks[1]]
    population[ind][picks[1]] = temp
    # print("Mutated path: ", population[ind])


# PMX crossover
def partially_matched_crossover(ind1, ind2):
    size = len(cities)
    p1, p2 = [0] * size, [0] * size

    # Initialize the position of each indices in the individuals
    for k in range(size):
        p1[ind1[k]] = k
        p2[ind2[k]] = k
    # Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    # Apply crossover between cx points
    for k in range(cxpoint1, cxpoint2):
        # Keep track of the selected values
        temp1 = ind1[k]
        temp2 = ind2[k]
        # Swap the matched value
        ind1[k], ind1[p1[temp2]] = temp2, temp1
        ind2[k], ind2[p2[temp1]] = temp1, temp2
        # Position bookkeeping
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return ind1, ind2


# function that picks a parent Fitness Proportionate Selection
def roulette_wheel_selection():
    s = 0
    partial_s = 0
    ind = 0
    for m in range(population_size):
        s = s + fitness[m]
    rand = random.uniform(0, s)
    for m in range(population_size):
        if partial_s < rand:
            partial_s = partial_s + fitness[m]
            ind = ind + 1
    if ind == population_size:  # prevent out of bounds list
        ind = population_size - 1
    return ind


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

    # print("Best route of generation", j + 1, ": ", population[find_fittest()], "\n" "Route length: ",
    #     routes_length[find_fittest()])
    # print("Population of generation", j + 1, ": \n", population)
    # print("Routes lengths:", routes_length, "\n")
print("Best path is:", population[index], "with length", best_path)
