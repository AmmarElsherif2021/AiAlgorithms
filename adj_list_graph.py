# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:20:59 2023

@author: ammar
"""
from collections import defaultdict

# 0- Node class
class Node:
    
    def __init__ (self,name,adj,cost,heu):
        self.name=name
        self.adj=list()
        self.cost=int()
        self.heu=int()
    
    def print_node(self):
        print((self.name,self.cost,self.heu))
        
    def setNodeEdges(self,x):
        self.adj=x
    
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
    nodeslist.append(newNode)  
print(nodelist)


# Represent an undirected graph  >>>>
    
#  1-Graph class

class Graph:
    
    #constructor
    def __init__ (self,nodes):
        
        # num of nodes
        self.N=nodes
        self.W_N=list()
        # Empty container for nodes >> a list for adjecency lists
        self.graph=defaultdict(list)
        
        # Fill the graph list
        for node in self.N :
            self.graph[node.name]
    
        
    
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
        '''
        for node in self.N:
            for i in range(len(self.N)):
                print('Now you inserts the node << ',node, ' >> adjacency: >> ')
                adj=input('Enter adjacency  >')
                if adj in self.N:
                    self.addEdge(node,adj)
                else:
                    break
       '''
        for node in self.N:
            print('Now you inserts the node ',node, ' adjacency: >> >>')
            adjacent=input('Enter adjacency  > ')
            adjList=adjacent.split(' ')
            for adj in adjList:
                #You can try it in recursive way for later >>
                #need to continue iteration from the error adj-insertion node .........
                if adj in self.N:
                    self.addEdge(node,adj)
                    
    #weighted Graph
    def addWeight(self):
        nodes=self.N
        w_nodes=list()
        for node in nodes:
            w_node={
                'node':node,
                'cost':0,
                'heu':0
                }
            print('For '+ node +' \n')
            w_node['cost']=input('INPUT COST: ')
            w_node['heu']=input('INPUT HEU: ')
            w_nodes.append(w_node)
        print(w_nodes,'\n')
        self.W_N=w_nodes
        return w_nodes
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

    

    # Greedy search for element x in graph
    def Greedy(self,x):
        q=['S']
        visited=['.']
        opened='' #--> expanded node var
        w_nodes=self.insertAdj() # --> weighted graph
        step_weights=list()    # --> weights of the q nodes in every step
        min_idx=int()
        
        
        if q and visited[0]!=x:
            # for node in q:
            #     step_weights.append(w_nodes[q.index(node)]['heu'])
            step_weights = [node.heu for node in w_nodes if node.node in q]
            print(step_weights)
            # min_idx=step_weights.index(min(step_weights))
            # if q[min_idx] in visited:
            #     q.pop(min_idx)
            #     print(q)
                
            # else:
            #     opened=q[min_idx]
            #     if self.graph[opened]:
            #         q.extend(self.graph[opened])
                    
            #     visited.append(opened)
            #     q.pop(min_idx)
            #     print(q)
                
        
            
                
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
                """
        
               
                        
    
    
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
nodes=[['S',1,1],['A',10,10],['B',7,7],['C',6,6],['D',5,5],['E',3,3],['F',2,2],['G',1,0]]
#nodesNames=['S','A','B','C','D','E','F','G']
nodeslist=[]
for node in nodes:
    
    
    name=node[0]
    cost=node[1]
    heu=node[2]
    newNode=Node(name,cost,heu)
    nodeslist.append(newNode)
    """
"""
for node in nodesName:
    
    print('\nType ',node,' cost\n')
    cost=int(input('>> '))
    
    print('\nType ',node,' heu\n')
    heu=int(input('>> '))
    
    newNode=Node(node,cost,heu)
    nodeslist.append(newNode)
"""  
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
#graph.DFS('G')
#graph.addWeight()
#graph.Greedy('G')
