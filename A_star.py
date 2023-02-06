# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:21:01 2023

@author: ammar
"""
#A* search Algorithm
#Greedy search Algorithm
#Hill Climbing Algorithm
from collections import defaultdict
from typing import Union
# 0- Node class
class Node:
    
    def __init__(self,name='',cost=0,heu=0):
        self.name=name
        self.adj=list()
        self.cost=cost
        self.heu=heu
    
    def print_node(self):
        print((self.name,self.cost,self.heu))
        
    def setNodeEdge(self,x):
        self.adj.append(x.getNode()[0])
   
    def getNodeEdges(self):
        return self.adj
    
    def getNode(self):
        return (self.name,self.cost,self.heu,self.adj)
    
#-create undir-graph----------------------------------------------------------------      
nodes=[['S',1,1],['A',10,10],['B',7,7],['C',6,6],['D',5,5],['E',3,3],['F',2,2],['G',1,0]]
#nodesNames=['S','A','B','C','D','E','F','G']
nodeslist=[] #graph input
for node in nodes:
    name=node[0]
    cost=node[1]
    heu=node[2]
    newNode=Node(name,cost,heu)
    nodeslist.append(newNode.getNode())  
#print(nodeslist)


# Represent an undirected graph  >>>>
    
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
            newNode=Node(node[0],node[1],node[2])
            self.graph[newNode]
    
        
    
    # function to print graph
    def print_graph(self):
        for node in self.graph:
            print(node.getNode())
    
    # function to return nodes names of graph:
    def getNodesNames(self):
        li=list()
        for node in self.N:
            li.append(node[0])
        
        return  li
    #function to search a node 
    def searchNode(self,x):
        for node in self.graph:
            if node.getNode()[0]==x:
                return node
           
            
    # function to make edge between 2 nodes s,d >> undirectional !!
    def addGraphNodeEdge(self,s:Node,d:Node)->None:
        
        if d.getNode()[0] not in s.getNodeEdges():
            s.setNodeEdge(d)
        else:
            print(d.getNode()[0] , ' is connected to ',s.getNode()[0])
        
        if s.getNode()[0] not in d.getNodeEdges():
            d.setNodeEdge(s)
        else:
            print(s.getNode()[0] , ' is connected to ',d.getNode()[0])
        
    
    #function to insert adjacencies of the whole graph :
    def insertAdjs(self):
        adjNode=Node()
        
        for node in self.graph:
            print('Now you inserts the node ',node.getNode()[0], ' adjacency: >> >>')
            adjacent=input('Enter adjacency  > ')
            adjList=adjacent.split(' ')
            for adj in adjList:
                #You can try it in recursive way for later >>
                #need to continue iteration from the error adj-insertion node .........
                if adj in self.getNodesNames():
                    adjNode=self.searchNode(adj)
                    self.addGraphNodeEdge(node,adjNode)
                else:
                    print('\n C MONNNN the node '+adj+' not in the graph [*__*] \n you need to Restart !!')
        
graph =Graph(nodeslist)
graph.insertAdjs()
graph.print_graph() 
