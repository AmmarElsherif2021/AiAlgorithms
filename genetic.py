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
population=100
w_limit=10
items=[]
gen_iteration=250
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

#parents indices selection
def selection(pop):
    new_n=int(0.85*(len(pop)-2))
    candidates_ix=np.random.randint(1, len(pop)-2, new_n).tolist()
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
    return [c1,c2]    


#mutate
def mutate(c):
    ix=randint(0,len(c)-1)
    c[ix]=1-c[ix]
    return c       

#evaluate, reproduce, mutate, crossover single generation of parents
def processGen(pop):
     
    score=list() # scores list
    new_pop=list()
        
    #all pop. objectives in each generation 
    score =[Obj(c) for c in pop]
    
    #sort items based on objectives
    score=sorted(score, key=lambda item: item['objValue'])   
    
    #and then alter pop list to 'individual' attribute in score
    pop=[c['individual'] for c in score]
    
    
    while score and score[0]['objValue']==0:
        del score[0]
        del pop[0]
    
        
    #1-reproduce
    if len(score)>2:
           new_pop.append(score[-2]['individual'])
                           
    if len(score)>1:
           new_pop.append(score[-1]['individual'])       
    #new_pop.extend([score[-1]['individual'],score[-2]['individual']])
    
    #2-mutate
    if len(score)>2:
        mutated=mutate(score[0]['individual'])
        new_pop.append(mutated)
    
    
    #3-crossover
    if len(pop)>4:
        crossoverable=list()
        crossoverable=selection(pop)
        counter=0 #counter to iterate to the middle of list of candidates to crossover
        half1_idx=int()
        half2_idx=int()
       
        while counter<int(len(crossoverable)/2):
            #random idx in the 1st half of crossoverable pop
            half1_idx=randint(0,int(len(crossoverable)/2)) 
            
            #random idx in the 2nd half of crossoverable pop
            half2_idx=randint(int(len(crossoverable)/2)+1,int(len(crossoverable)))
            
            new_pop.extend(crossover(pop[half1_idx],pop[half2_idx]))
            counter+=1
    
    return new_pop

#iterate generations and produce selected individual
def geneticFun(weights,values,population,w_limit,gen_iteration):
    #generate population
    pop=generatePop(len(weights),population)
    #generation iterations
    gen_counter=0
    
    while gen_counter<gen_iteration and len(pop)>1:
        pop=processGen(pop)
        print('Generation number >> ',gen_counter)
        print(pop)
        gen_counter+=1
    
    print('weights selected >> ',interpretElected(pop[0]))
    return pop
 
# interpret the individual into a meaning decision 
def interpretElected(c):
    output=[a*b for a,b in zip(c,weights)]
    return output
if __name__=='__main__':
    #test
   
    #print(crossover([1,0,1,0],[0,1,0,1]))
    geneticFun(weights,values,population,w_limit,gen_iteration)
