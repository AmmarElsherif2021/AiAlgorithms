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
    
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
    def getItem(self):
        return [self.weight,self.value]
'''
#list of items
weights=[1,2,4,2,5]
values=[5,3,5,3,2]
population=20
w_limit=10
items=[]
'''
for i in range(len(weights)):
    items.append(knapsackItem(weights[i],values[i]))
'''
#Genetic Algorithm implementation
def generatePop(n_bits,n_pop):
    pop=[np.random.randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    return pop

#Objective function to calc score
def Obj(individual):
    #if over-weight set then limitedWeight=0
    limitedWeight=int(np.dot(individual,weights)<=w_limit) 
    #net values of limited weighted items in the knapsack
    objValue=np.dot(values,individual)*limitedWeight
    return {'individual':individual,
            'objValue':objValue}

       
#process generations
def evalGen(n_itr):
    pop=generatePop(len(weights),population) 
    score=list() # scores list
    
        
    for gen in range(n_itr):
        #all pop. in each generation 
        score =[Obj(c) for c in pop]
        
        #sort items based on objectives
        score=sorted(score, key=lambda item: item['objValue'])   
        
        while score[0]['objValue']==0:
            del score[0]
        
        #1-reproduce
        
        #2-mutate
        
        #3-crossover
    
    return score

#parents indices selection
def selection(pop):
    candidates_ix=np.random.randint(1, len(pop)-2, 4).tolist()
    return candidates_ix
#cross over two parents
def crossover(c1,c2):
    #play toss for each gene in th chromosome -->uniform crossover
    cross=bool()
    temp=int()
    for i in range(len(c1)):
        cross=bool(randint(0,1))
        if cross:
            temp=c1[i]
            c1[i]=c2[i]
            c2[i]=temp
        


#mutate
def mutate(c):
    ix=randint(0,len(c)-1)
    c[ix]=1-c[ix]
    
#test
print(evalGen(5))
print(crossover([1,0,1,0],[0,1,0,1]))