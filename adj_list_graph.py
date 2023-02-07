# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:20:59 2023

@author: ammar
"""
from collections import defaultdict
from graph import Node,Graph


#Breadth first search----------------------------------------------------


def BFS(graph,x):
    q=['S']
    visited=['.']
    opened=''
    openedNode=Node()
    
    for node in graph.getNodes():
        print(node.getNodeEdges())
    while q and visited[0]!=x:
        if q[0] in visited:
            q.pop(0)
            print(q)
            
        else:
            opened=q[0]
            print('opened-->',opened)
            
            openedNode=Node()
            if opened in graph.getNodesNames():
                openedNode=graph.searchNode(opened)
                q.extend(openedNode.getNodeEdges())
                print('extended---',openedNode.getNodeEdges())
                visited.append(opened)
                print('visited --> ',visited)
                q.pop(0)
            
            print(q)
            
    print('\n')            
    print(int(visited[-1]==x)*('congrats it worked\n'))
    print(int(visited[-1]!=x)*('OooPS Missed it !! !! \n'))
    print(visited) 
 
# DFS search value x in graph

def DFS(graph,x):
    stack=['S']
    visited=['.']
    opened=''
   
    while stack and visited[-1]!=x :
        if stack[-1] in visited:
            stack.pop(-1)
            print('STACK --> ',stack)
            
        else:
            opened=stack[-1]
            openedNode=Node()
            stack.pop(-1)
            
            if opened in graph.getNodesNames():
                openedNode=graph.searchNode(opened)
                li=openedNode.getNodeEdges()
                for node in list(reversed(li)):
                    if node not in visited:
                        stack.append(node)
                    
                
                visited.append(opened)    
                
               
            print('STACK ----> ',stack)
            
    
    print('\n')            
    print(int(visited[-1]==x)*('congrats it worked\n'))
    print(int(visited[-1]!=x)*('OooPS Missed it !! !! \n'))
    print(visited) 

 

# Greedy search for element x in graph
def Greedy(graph,x):
    stack=['S']
    visited=['.']
    opened=''
   
    # A function to sort list of nodes names based on their heu
    def descendentHue(li):
        nodesHueList=list()
        returnlist=list()
        heu=int()
        for node in li:
            heu=graph.searchNode(node).getNode()[1]
            nodesHueList.append([node,heu])
        nodesHueList.sort(key=lambda x: x[1])
        for node in nodesHueList:
            returnlist.append(node[0])
        return returnlist

    
    while stack and visited[-1]!=x :
        if stack[-1] in visited:
            stack.pop(-1)
            print('STACK --> ',stack)
            
        else:
            opened=stack[-1]
            openedNode=Node()
            stack.pop(-1)
            
            if opened in graph.getNodesNames():
                openedNode=graph.searchNode(opened)
                edgelist=openedNode.getNodeEdges()
                huelist=descendentHue(edgelist)
                # li.sort(reverse=True)
                for node in huelist:
                    if node not in visited:
                        stack.append(node)
                visited.append(opened)    
                print('VISITED ==>',visited)
               
            print('STACK ----> ',stack)
            
    
    print('\n')            
    print(int(visited[-1]==x)*('congrats it worked\n'))
    print(int(visited[-1]!=x)*('OooPS Missed it !! \n'))
    print('visited --->> ',visited) 
             
     
         
             
        

# Represent an undirected graph  >>>>

"""
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
                """
        
               
                        
'''
    
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
    '''
#-----------------------------------------------------------------------
      
#-create undir-graph----------------------------------------------------------------      
nodes=[['S',1],['A',5],['B',7],['C',6],['D',5],['E',3],['F',2],['G',0]]
#nodesNames=['S','A','B','C','D','E','F','G']
nodeslist=[] #graph input
for node in nodes:
    name=node[0]
    hue=node[1]
    newNode=Node(name,hue)
    nodeslist.append(node)  
print(nodeslist)    

graph=Graph(nodeslist)
graph.insertAdjs()
#-Excute search methods:

BFS(graph,'G')
DFS(graph,'G')

Greedy(graph,'G')
