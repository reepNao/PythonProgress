"""
Graph:
------
    - A graph is a non-linear data structure consisting of nodes and edges.
    - The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph.
    - More formally a Graph can be defined as,
    - A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.
    - In the above Graph, the set of vertices V = {0,1,2,3,4} and the set of edges E = {01, 12, 23, 34, 04, 14, 13}.
    - Graphs are used to solve many real-life problems.
    - Graphs are used to represent networks.
    - The networks may include paths in a city or telephone network or circuit network.
    - Graphs are also used in social networks like linkedIn, Facebook.
    - For example, in Facebook, each person is represented with a vertex(or node).
    (Vertex = Node, Edge = Line, Arc or Connection)

"""


class Graph:

    def __init__(self):
        self.adjdict = {}

    def addVertex(self, vertex):
        if vertex not in self.adjdict.keys():
            self.adjdict[vertex] = []
            return True
        return False

    def addEdge(self, v1, v2):
        if v1 in self.adjdict.keys() and v2 in self.adjdict.keys():
            self.adjdict[v1].append(v2)
            self.adjdict[v2].append(v1)
            return True
        return False
    
    def removeEdge(self, v1, v2):
        if v1 in self.adjdict.keys() and v2 in self.adjdict.keys():
            try:
                self.adjdict[v1].remove(v2)
                self.adjdict[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjdict.keys():
            for key in self.adjdict[vertex]:
                self.adjdict[key].remove(vertex)
            del self.adjdict[vertex]
            return True
        return False

    def printGraph(self):
        for key in self.adjdict:
            print(key, '->', self.adjdict[key])

mygraph = Graph()
mygraph.addVertex('IST')
mygraph.addVertex('SFO')
mygraph.addVertex('ORD')
mygraph.addVertex('LAX')
mygraph.addVertex('DFW')

mygraph.addEdge('IST', 'SFO')
mygraph.addEdge('IST', 'ORD')
mygraph.addEdge('IST', 'LAX')
mygraph.addEdge('LAX', 'DFW')
mygraph.addEdge('DFW', 'ORD')
mygraph.addEdge('DFW', 'SFO')

mygraph.printGraph()

print('-------------------')

mygraph.removeEdge('IST', 'SFO')
mygraph.removeVertex('DFW')

mygraph.printGraph()



#reorder routes to make all paths lead to thw city zero
#n = 6 c =[[0,1], [1,3], [2,3], [4,0], [4,5]]
#n = 5 c = [[1,0], [1,2], [3,2], [3,4]]


class Solution:
    def minReorder(self, n, Connections):
        edges = set()

        for a,b in connections:
            edges.add((a,b))

        neighbours = {}

        for city in range(n):
            neighbours[city] = []

        for a,b in coonectipns:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()
        counter = 0

        def dfs(city):
            nonlocal counter, neighbours, visited, edges
            for neigbour in neighbours[city]:
                if neigbour in visited:
                    continue
                if (city, neigbour) in edges:
                    counter += 1
                visited.add(neigbour)
                dfs(neigbour)
        
        visited.add(0)
        dfs(0)
        return counter

#Number of Islands
#Given a m * n 2d grid map of '1's (land) and '0's (water), count the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

class IslandSolution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rowNumber = len(grid)
        columnNumber = len(grid[0])
        
        visited = set()
        
        islandCounter = 0
        
        def bfs(row,column):
            myQueue = []
            
            visited.add((row,column))
            myQueue.append((row,column))
            
            
            while len(myQueue) != 0:
                row,column = myQueue.pop(0)
                myDirections = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for rowDirection, columnDirection in myDirections:
                    newRow = row + rowDirection
                    newColumn = column + columnDirection
                    
                    if(newRow in range(rowNumber) and newColumn in range(columnNumber) and
                       grid[newRow][newColumn] == "1" and (newRow, newColumn) not in visited):
                        myQueue.append((newRow, newColumn))
                        visited.add((newRow, newColumn))
                        
            
        for row in range(rowNumber):
            for column in range(columnNumber):
                if grid[row][column] == "1" and (row,column) not in visited:
                    bfs(row,column)
                    islandCounter += 1
                        
        return islandCounter

sol = IslandSolution()
grid = [['1', '1', '0', '0', '0'], 
        ['1', '1', '0', '0', '0'], 
        ['0', '0', '1', '0', '0'], 
        ['0', '0', '0', '1', '1']]
print(sol.numIslands(grid))


#Reduntant Connection
#In this problem, a tree is an undirected graph that is connected and has no cycles.
#UNion find algorithms

class ReduntantSolution:
    def findReduntantConnection(self, edges):
        parents = []
        for i in range(len(edges)+1):
            parents.append(i)

        rank = [1] * (len(edges)+1)

        def find(n):
            parent = parents[n]
            while parent != parents[parent]:
                #path  compression
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent

        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)

            if parent1 == parent2:
                #connected
                return False
            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

sol = ReduntantSolution()
edges = [[1,2], [1,3], [2,3]]
print(sol.findReduntantConnection(edges))
edges2 = [[1,2], [1,3], [1,4], [1,5], [4,5]]
print(sol.findReduntantConnection(edges2))