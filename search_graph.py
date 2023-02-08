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
                
                for node in openedNode.getNodeEdges():
                    if node not in visited:
                        q.append(node)
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

#Uniform cost Algorithm | Dijkstra’s single-source-shortest-path algorithm: 
def UCS(graph,x):
    q=['S']
    visited=['.']
    opened=''
    openedNode=Node()
    sortedCostList=list()
    
    #------------------------------------
    def ascendentCost(li):
        
        nodesCostList=list()
        returnlist=list()
        for node in li:
            nodesCostList.append(graph.searchNode(node).getNodeCostedEdges())

        nodesCostList.sort(key=lambda x: x[1])
        for node in nodesCostList:
            returnlist.append(node[0])
        return returnlist
    
    #-------------------------------------
    
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
                
                for node in openedNode.getNodeEdges():
                    if node[0] not in visited:
                        q.append(node[0])
                
                
                
                print('extended---',openedNode.getNodeEdges())
                visited.append(opened)
                print('visited --> ',visited)
                q.pop(0)
                #Arrange queue based on costs
            q=ascendentCost(q)    
            print(q)
            
    print('\n')            
    print(int(visited[-1]==x)*('congrats it worked\n'))
    print(int(visited[-1]!=x)*('OooPS Missed it !! !! \n'))
    print(visited)
             
#A* search Algorithm         
def A_star(graph,x):
    pass

#Hill climbing search Algorithm
def hill_climbing(graph,x):
    pass
        




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

# test graph edges existance:
'''
for node in graph.getNodes():
    print(node.getNode(),'---->',node.getNodeCostedEdges())
'''
#-Excute search methods:

#BFS(graph,'G')
#DFS(graph,'G')
#Greedy(graph,'G')
UCS(graph, 'G')