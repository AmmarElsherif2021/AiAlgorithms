from graph import Node,Graph
from search_graph import hill_climbing
matrix=[[0,1,2,3,5,8],
        [2,3,5,7,9,10],
        [4,6,7,10,11,12],
        [5,9,10,12,13,15],
        [6,10,13,15,17,20]]
def createGraph():
    temp=Node()
    name=''
    inputList=list()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            #append node in input list of the graph >>
            name=str(i)+str(j)
            inputList.append([name,matrix[i][j]])
    
    graph=Graph(inputList)
           
    '''
            if matrix[i][j+1]:
                pass
            if matrix[i+1]:
                pass
            '''
    
    return graph
graph=createGraph()
print(graph.print_graph())
def addAdj(graph):
    adjNode=Node()
    isCosted= True
    name=''
    for node in graph:
        print('node ',node.getNode()[0], ' adjacencies: >> >>')
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j+1]:
                    pass
                if matrix[i+1]:
                    pass
        
        '''
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
        '''