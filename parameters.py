from file import read_data
from matrix import create_matrix

path_holder = []
population_size = 20
mutate_prob = 0.2
n_generations = 5
routes_length = [0] * population_size
fitness = [0] * population_size
best_path = 1000
data = read_data('a280.txt')
distances = create_matrix(data)