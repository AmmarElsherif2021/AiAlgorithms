# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:20:59 2023

@author: ammar
"""
# Represent a graph>>

#  1- Node class

class Node:
    def __init__ (self,data):
        self.node=data
        self.next=None
    
#  2-Graph class

class Graph:
    
    #constructor
    def __init__ (self,nodes):
        
        # num of nodes
        self.N=nodes
        
        # Empty container for nodes >> a list for adjecency lists
        self.graph=[None]*self.N
    
    # function to make edges between nodes
    def addEdge(self,source,dest):
        
        

