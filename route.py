# creates a random route
import random


def create_route(cities):
    shuffled = random.sample(cities, len(cities))
    return shuffled

