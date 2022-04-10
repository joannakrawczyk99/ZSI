# PMX crossover
import random


def crossover(ind1, ind2, cities):
    size = len(cities)
    p1, p2 = [0] * size, [0] * size

    for k in range(size):
        p1[ind1[k]] = k
        p2[ind2[k]] = k
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    for k in range(cxpoint1, cxpoint2):
        temp1 = ind1[k]
        temp2 = ind2[k]
        ind1[k], ind1[p1[temp2]] = temp2, temp1
        ind2[k], ind2[p2[temp1]] = temp1, temp2
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return ind1, ind2