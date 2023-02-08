# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:21:01 2023

@author: ammar
"""
import itertools
from collections import defaultdict
from typing import Union
# 0- Node class
class Node:
    
    def __init__(self,name='',heu=0):
        self.name=name
        self.adj=list()
        
        self.heu=heu
    
    def print_node(self):
        print((self.name,self.heu))
        
    def setNodeEdge(self,x,cost=0):
        self.adj.append([x.getNode()[0],cost])
   
    def getNodeEdges(self):
        li=list()
        for node in self.adj:
            li.append(node[0])
        return li
    
    def getNodeCostedEdges(self):
        return self.adj
    
    def getNode(self):
        return (self.name,self.heu,self.adj)
    



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
            newNode=Node(node[0],node[1])
            self.graph[newNode]
    
        
    
    # function to print graph
    def print_graph(self):
        for node in self.graph:
            print(node.getNode())
    
    # function to return list of actual nodes:
    def getNodes(self):
        return self.graph
    
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
    def addGraphNodeEdge(self,s:Node,d:Node,cost:int)->None:
        
        if d.getNode()[0] not in s.getNodeEdges():
            s.setNodeEdge(d,cost)
        else:
            print(d.getNode()[0] , ' is connected to ',s.getNode()[0])
        
        if s.getNode()[0] not in d.getNodeEdges():
            d.setNodeEdge(s,cost)
        else:
            print(s.getNode()[0] , ' is connected to ',d.getNode()[0])
        
    
    #function to insert adjacencies of the whole graph :
    def insertAdjs(self):
        adjNode=Node()
        isCosted=bool()
        costed=input('Are Graph edges costed ? y/n > ')
        isCosted= True if costed =='y' else False
        
        for node in self.graph:
            print('Now you insert the node ',node.getNode()[0], ' adjacencies: >> >>')
            adjacent=input('Enter adjacencies  > ')
            cost=input('Enter adj cost > ') if isCosted==True else 0
           
            adjList=adjacent.split(' ')
            
            costList=[int(c) for c in cost.split(' ')] if isCosted else [0]*len(adjList)
            for i in range(len(adjList)):
                #You can try it in recursive way for later >>
                #need to continue iteration from the error adj-insertion node .........
                if adjList[i] in self.getNodesNames():
                    adjNode=self.searchNode(adjList[i])
                    self.addGraphNodeEdge(node,adjNode,costList[i])
                else:
                    print('\n C MONNNN the node '+adjList[i]+' not in the graph [*__*] \n you need to Restart !!')
        #--------------------------------------------------------
    
    def getCost(self,a,b):
        A=self.searchNode(a).getNode()
        for node in A[2]:
            if node[0]==b:
                return int(node[1])
        
        
        

#Test : -----------------------------------       
