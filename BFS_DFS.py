#BFS Algorithm implementation:
# Adjacency Matrix representation in Python
import pandas as pd

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, x, y):
        if x == y:
            print("Same vertex %d and %d" % (x, y))
        self.adjMatrix[x][y] = 1
        self.adjMatrix[y][x] = 1

    # Remove edges
    def remove_edge(self, x, y):
        if self.adjMatrix[x][y] == 0:
            print("No edge between %d and %d" % (x, y))
            return
        self.adjMatrix[x][y] = 0
        self.adjMatrix[y][x] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        df=pd.DataFrame(self.adjMatrix)
        print(df)
        print(self.adjMatrix)
        
    def dfs_func(self):
        visited_nodes=(self.adjMatrix)
        for i in range(self.size):
            for j in range(self.size):
                if visited_nodes[i][j]==1:
                    visited_nodes[i][j]=0
        
        
        q=[(0)]
        
        
        
        print(visited_nodes)
        
        
        
        
            


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()
    g.dfs_func()

if __name__ == '__main__':
    main()
