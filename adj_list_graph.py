# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:20:59 2023

@author: ammar
"""
from collections import defaultdict
# Represent an undirected graph>>
    
#  1-Graph class

class Graph:
    
    #constructor
    def __init__ (self,nodes):
        
        # num of nodes
        self.N=nodes
        
        # Empty container for nodes >> a list for adjecency lists
        self.graph=defaultdict(list)
        
        # Fill the graph list
        for node in self.N :
            self.graph[node]
    
   
    
   # function to print graph
    def print_graph(self):
        for node in self.N:
            print(node,' -->',self.graph[node])
    
   
    
   # function to make edges between nodes
    def addEdge(self,s,d):
        if d not in self.graph[s]:
            self.graph[s].append(d)
        else:
            print(d , ' is connected to ',s)
        
        if s not in self.graph[d]:
            self.graph[d].append(s)
        else:
            print(s , ' is connected to ',d)
    
    #function to insert adjacencies:
    def insertAdj(self):
        for node in self.N:
            for i in range(len(self.N)):
                print('Now you inserts the node ',node, ' adjacency: >> >>')
                adj=input('Enter adjacency')
                if adj in self.N:
                    graph.addEdge(node,adj)
                else:
                    break

        
Nodes=['A','B','C','D','E']
graph =Graph(Nodes)
graph.insertAdj()
graph.print_graph()


