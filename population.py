# creates starting population
from main import population_size, population
from route import create_route


def create_population():
    for i in range(population_size):
        population.append(create_route())
