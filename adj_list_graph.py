# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:20:59 2023

@author: ammar
"""
from collections import defaultdict
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
                print('Now you inserts the node << ',node, ' >> adjacency: >> ')
                adj=input('Enter adjacency  >')
                if adj in self.N:
                    self.addEdge(node,adj)
                else:
                    break
    
    # BFS search value x in graph
    def BFS(self,x):
        q=['S']
        visited=['.']
        opened=''
        while q and visited[0]!=x:
            if q[0] in visited:
                q.pop(0)
                print(q)
                
            else:
                opened=q[0]
                if self.graph[opened]:
                    q.extend(self.graph[opened])
                    
                visited.append(opened)
                q.pop(0)
                print(q)
                
        
            
                
        print('\n')            
        print(int(visited[-1]==x)*('congrats it worked\n'))
        print(int(visited[-1]!=x)*('Sorry !! \n'))
        print(visited)
    
    # DFS search value x in graph
    def DFS(self,x):
        stack=['S']
        visited=['.']
        opened=''
       
        while stack and visited[0]!=x :
            if stack[-1] in visited:
                stack.pop(-1)
                print(stack)
                
            else:
                opened=stack[-1]
                stack.pop(-1)
                
                if self.graph[opened]:
                    for newNode in (self.graph[opened]):
                        if newNode not in visited:
                            stack.append(newNode)
                            break
                    
                    
                print(stack)
                visited.append(opened)
        
        print('\n')            
        print(int(visited[-1]==x)*('congrats it worked\n'))
        print(int(visited[-1]!=x)*('Sorry !! \n'))
        print(visited)
#  Directional Graph ---> Note: state space could be presented using DiGraph

class DiGraph:
    
    # constructor
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
        

    # function to insert adjacencies:
    def insertAdj(self):
        for node in self.N:
            for i in range(len(self.N)):
                print('Now you inserts the node ',node, ' adjacency: >> >>')
                adj=input('Enter adjacency  > ')
                if adj in self.N:
                    self.addEdge(node,adj)
                else:
                    break
    
    
    # BFS search value x in graph
    def BFS(self,x):
        q=['S']
        visited=['.']
        
        while q and visited[0]!=x:
            for node in self.graph:
                if q[0] in visited:
                    del q[0]
                    
                else:
                    for adj in self.graph[node]:
                        q.append(adj)
                        print(q)
                    visited.append(q[0])
                    del q[0]
        
            
                
        print('\n')            
        print(int(visited[-1]==x)*('congrats it worked\n'))
        print(int(visited[-1]!=x)*('Sorry !! \n'))
        print(visited)
    
    # DFS search value x in graph
    def DFS(self,x):
        stack=['S']
        visited=['.']
        opened=''
       
        while stack and visited[0]!=x :
            if stack[-1] in visited:
                del stack[-1]
                
            else:
                opened=stack[-1]
                del stack[-1]
                if self.graph[opened]:
                    stack.append(self.graph[opened][0])
                    
                print(stack)
                visited.append(opened)
                

        print('\n')            
        print(int(visited[-1]==x)*('congrats it worked\n'))
        print(int(visited[-1]!=x)*('Ooops Blocked!! \n'))
        print(visited)
    
#-----------------------------------------------------------------------
      
    
#-create undir-graph----------------------------------------------------------------      
Nodes=['S','A','B','C','D','E','F','G']
graph =Graph(Nodes)
graph.insertAdj()
graph.print_graph()

#-create dir-graph

"""
dirgraph =DiGraph(Nodes)
dirgraph.insertAdj()
dirgraph.print_graph()

"""

#-Excute search methods:
    
#dirgraph.BFS('F')
#dirgraph.DFS('F')
#graph.BFS('G')
graph.DFS('G')