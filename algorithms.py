from random import random


# Weighted Random Shuffle
# based on Weighted Random Sampling (2005; Efraimidis, spirakis)
def WRS(items, weights):
    order = sorted(range(len(items)), key=lambda i: random.random() ** (1.0 / weights[i]))
    return [items[i] for i in order]
