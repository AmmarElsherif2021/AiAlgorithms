# Python code to for DFS
from collections import defaultdict


class Graph:

    # list Constructor 
    def __init__(self):

        # default dictionary to store nodes
        self.graph = defaultdict(list)

    # add edge to the graph
    def addingEdge(self, x, y):
        self.graph[x].append(y)

    # BFS function to print nodes
    def BFSfunction(self, n):

        # Initially marking all vertices as not visited
        visited_vertices = (len(self.graph)) * [False]

        # create a queue for visited nodes
        queue = []

        # setting source node as visited and add it to the queue
        visited_vertices[n] = True
        queue.append(n)

        while queue:

            # # pop visited elements from the queue
            n = queue.pop(0)
            print(n, end=" ")

            # get adjacent vertices to the vertex n which is dequeued.
            for v in self.graph[n]:
                if visited_vertices[v] == False:
                    queue.append(v)
                    visited_vertices[v] = True

# Create a graph


graph = Graph()
graph.addingEdge(0, 1)
graph.addingEdge(1, 1)
graph.addingEdge(2, 3)
graph.addingEdge(3, 1)
graph.addingEdge(4, 2)
graph.addingEdge(5, 4)

print("DFS Search return")
graph.BFSfunction(0)