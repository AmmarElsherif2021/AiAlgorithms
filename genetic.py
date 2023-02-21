from random import randint
import numpy as np
'''
problem:- a collection of stuff that you gonna put in a knapsack.
        - a knapsack is limited in ceratin capacity of weights. 
        - each item has a value for 1 kg differs from other items values.
        - you gotta maximize the value of whole items carried in the knapsack.
'''
# create Knapsack item class
'''
class knapsackItem:
    def __init__(self,index,weight,value):
        self.index=index
        self.weight=weight
        self.value=value
    def getItem(self):
        return [self.index,self.weight,self.value]
'''
#list of items
weights=[1,2,4,2,5]
values=[5,3,5,3,2]
population=20
w_limit=10
#Genetic Algorithm implementation
def generatePop(n_bits,n_pop):
    pop=[np.random.randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    return pop

#Objective function to calc score
def Obj(individual):
    #if over-weight set then limitedWeight=0
    limitedWeight=int(np.dot(individual,weights)<=w_limit) #---> modify 10 value(1)
    #net values of limited weighted items in the knapsack
    objValue=np.dot(values,individual)*limitedWeight
    return objValue

#process generations
def evalGen(n_itr):
    pop=generatePop(len(weights),population) 
    score=list() # scores list
    for gen in range(n_itr):
        #evaluate all pop. in each generation
        score=[Obj(c) for c in pop]
        score.sort()
        
    return (pop,score)

#test
print(evalGen(5))