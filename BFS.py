#author: Ammar
# Python code to for BFS
from collections import defaultdict


class Graph:

    # Graph Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add edge to the graph
    def addEdge(self, x, y):
        self.graph[x].append(y)
        print(self.graph)

    # BFS function to printing nodes
    def BFSfunc(self, n):

        # Initially marking all vertices as not visited
        visited = (len(self.graph)) * [False]

        # create a queue for visited nodes
        queue = []

        # setting source node as visited and add it to the queue
        visited[n] = True
        queue.append(n)

        while queue:

            # pop visited elements from the queue 
            n = queue.pop(0)
            print(n, end=" ")

            # get adjacent vertices to the vertex n which is dequeued.
            for v in self.graph[n]:
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = True
            
            print(visited)

# Create graph


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 2)
graph.addEdge(3, 1)
graph.addEdge(4, 3)
graph.addEdge(5, 4)

print("BFS return:")
graph.BFSfunc(0) 