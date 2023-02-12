# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:20:59 2023

@author: ammar

reference:https://medium.com/nerd-for-tech/ai-search-algorithms-with-examples-54772c6d973a
"""
from collections import defaultdict
from graph import Node,Graph


#Breadth first search----------------------------------------------------


def BFS(graph,x):
    print('BFS -------------------------------')
    q=['S']
    visited=['.']
    opened=''
    openedNode=Node()
    
    for node in graph.getNodes():
        print(node.getNodeEdges())
    while q and visited[-1]!=x:
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
    print('DFS --------------------------------------')
    stack=['S']
    visited=['.']
    opened=''
   
    while stack and visited[-1]!=x :
        if stack[-1] in visited:
            stack.pop(-1)
            print('visited -->',visited)
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
                
            print('visited---->',visited)   
            print('STACK ----> ',stack)
            
    
    print('\n')            
    print(int(visited[-1]==x)*('congrats it worked\n'))
    print(int(visited[-1]!=x)*('OooPS Missed it !! !! \n'))
    print(visited) 

 

# Greedy search for element x in graph
def Greedy(graph,x):
    print('GREEDY -------------------------------')
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
        nodesHueList.sort(key=lambda x: x[1] ,reverse=True)
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
    print('UCS -------------------------------------')
    q=[['S',0]]
    visited=['.']
    opened=''
    openedNode=Node()
    sortedCostList=list()
    
    #function to arrange queue nodes based on cost------------------------------------
    def ascendentCost(nodesCostList):
        nodesCostList.sort(key=lambda x: x[1] , reverse=False)
        return nodesCostList
    
    #-------------------------------------
    #cost of expanded node to be accumulated
    expandedCost=0
    while q and visited[-1]!=x:
        
       
        #opened node name 
        opened=q[0][0]
        #print('opened-->',opened)
        
        openedNode=Node()
        if opened in graph.getNodesNames():
            openedNode=graph.searchNode(opened)
            expandedCost=q[0][1]
            for node in openedNode.getNodeCostedEdges():
                #even if expanded node in visited append the visiteed 
                q.append([node[0],node[1]+expandedCost])
            
            
            
            print('extended---',openedNode.getNodeEdges())
            visited.append(opened)
            print('visited --> ',visited)
            q.pop(0)
        
        
        #Arrange queue based on costs
        q=ascendentCost(q)    
        print('Periority Queue -->',q)     
            
    print('\n')            
    print(int(visited[-1]==x)*('congrats it worked\n'))
    print(int(visited[-1]!=x)*('OooPS Missed it !! !! \n'))
    print('checked nodes --->',visited)
    opt_path=list()
    reversedVisited=visited
    reversedVisited.pop(0)
    reversedVisited.reverse()
    temp=Node()
    
    for node in reversedVisited:
        temp=graph.searchNode(node)
        if len(opt_path)==0:
            opt_path.append(node)
        elif opt_path[-1] in temp.getNodeEdges():
            opt_path.append(node)
        
    
    print('opt. path--->',opt_path)
      
        
#A* search Algorithm         
def A_star(graph,x):
    q=[['S',0]]
    visited=['.']
    opened=''
    openedNode=Node()
    sortedCostList=list()
    
    #------------------------------------
    def ascendentCost(nodesCostList):
        nodesCostList.sort(key=lambda x: x[2])
        return nodesCostList
    #........
    def replaceToMinFun(newNode,q):
        if any(newNode in sublist for sublist in q):
            for node in q:
                if newNode[0]==node[0]:
                    if newNode[2]<node[2]:
                        node=newNode
        else:
            q.append(newNode)
            
        
                
    #-------------------------------------
    
    
    expandedCost=0
    while q and visited[-1]!=x:
        if q[0][0] in visited:
            q.pop(0)
            print('visited popped -->',q)
            
        else:
            opened=q[0][0]
            print('opened-->',opened)
            
            openedNode=Node()
            if opened in graph.getNodesNames():
                openedNode=graph.searchNode(opened)
                expandedCost=q[0][1] 
                for node in openedNode.getNodeCostedEdges():
                    if node[0] not in visited:
                        heu=graph.searchNode(node[0]).getNode()[1]
                        newToQ=[node[0],node[1]+expandedCost,heu+node[1]+expandedCost]
                        replaceToMinFun(newToQ, q)
                        

                #print('extended---',openedNode.getNodeEdges())
                visited.append(opened)
                print('visited --> ',visited)
                q.pop(0)
            
            
            #Arrange queue based on costs
            q=ascendentCost(q)    
            print('---> Q: ',q)
            
    print('\n')            
    print(int(visited[-1]==x)*('congrats it worked\n'))
    print(int(visited[-1]!=x)*('OooPS Missed it !! !! \n'))
    print(visited)
    #----
    opt_path=list()
    reversedVisited=visited
    reversedVisited.pop(0)
    reversedVisited.reverse()
    temp=Node()
    
    for node in reversedVisited:
        temp=graph.searchNode(node)
        if len(opt_path)==0:
            opt_path.append(node)
        elif opt_path[-1] in temp.getNodeEdges():
            opt_path.append(node)
        
    opt_path.reverse()
    print('opt. path--->',opt_path)

                
#Hill climbing search Algorithm (or Gradient Descent):
def hill_climbing(graph,x):
    pass
        




#-----------------------------------------------------------------------
      
#-create undir-graph----------------------------------------------------------------      

nodes=[['S',5],['A',16],['B',10],['C',12],
       ['D',14],['E',9],['F',10],['G',8],
       ['H',10],['I',8],['J',6],['K',5],['L',4],['M',0]
       ]
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

#BFS(graph,'M')
#DFS(graph,'M')
#Greedy(graph,'M')
#UCS(graph, 'M')
#A_star(graph, 'M')