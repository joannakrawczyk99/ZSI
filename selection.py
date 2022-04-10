# function that picks a parent Fitness Proportionate Selection
import random


def roulette_wheel_selection(population_size, fitness):
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
