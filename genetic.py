from random import randint
import numpy as np
'''
problem:- a collection of stuff that you gonna put in a knapsack.
        - a knapsack is limited in ceratin capacity of weights. 
        - each item has a value for 1 kg differs from other items values.
        - you gotta maximize the value of whole items carried in the knapsack.
'''
#Genetic Algorithm implementation
def generatePop(n_bits,n_pop):
    pop=[np.random.randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    return pop

#test
print(generatePop(4,20))