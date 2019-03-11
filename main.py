from BuildGraph import Graph
from BuildGraph import readinFile
from Vertex import Vertex

vertices = []

def makeSet(name):
    for i in range(len(vertices)):
        if name == vertices[i].name:
            return

    vertex = Vertex()
    vertex.name = name
    vertex.root = name
    vertex.rank = 0
    vertices.append(vertex)


def find(vertexName):
    for i in range(len(vertices)):
        if vertexName == vertices[i].name:                      # If root is itself, then return index, at top of tree
            if vertices[i].name == vertices[i].root:
                return i
            return find(vertices[i].root)                       # If root is not the same as vertex, return until it is


def union(vertex1, vertex2):
    index1 = find(vertex1)
    index2 = find(vertex2)

    if vertices[index1].root == vertices[index2].root:        # X and Y are in the same set, returning without adding
        return 0

    if vertices[index1].rank < vertices[index2].rank:         # X and Y are not in the same set, merge them
        vertices[index1].root = vertices[index2].root
        return 1
    elif vertices[index1].rank > vertices[index2].rank:
        vertices[index2].root = vertices[index1].root
        return 1
    else:
        vertices[index2].root = vertices[index1].root
        vertices[index1].rank +=1
        return 1

def kruskal(V, G):


    MST = []
    keys = list(G.keys())
    edges = []
    weight = 0

    for i in range(0, len(keys)):
        for j in range(0, len(G[keys[i]])):
            edges.append([keys[i], G[keys[i]][j][0], G[keys[i]][j][1]])         # Pull everything from dictionary and put into an array

    edges = sorted(edges, key=lambda item: int(item[2]))                        # Sort edges array by weight

    for i in range(0, len(edges)):                                              # Make sets of all vertices
        if edges[i][0] not in vertices:
            makeSet(edges[i][0])

    while len(MST) < V - 1:
        for e in range(0, len(edges)):
            if len(MST) < V - 1:
                ret = union(edges[e][0], edges[e][1])
                if ret == 1:
                    MST.append(edges[e])
                    weight += int(edges[e][2])

    print("Total Weight: ", weight)
    return MST


myGraph = Graph()
readinFile(myGraph, "city-pairs.txt")
MST = kruskal(myGraph.V, myGraph.graph)
for i in MST:
    print(i)

vertices = []
graph2 = Graph()

graph2.addEdge('A','B',3)
graph2.addEdge('B','A',3)
graph2.addEdge('A','D',2)
graph2.addEdge('D','A',2)
graph2.addEdge('B','C',4)
graph2.addEdge('C','B',4)
graph2.addEdge('C','D',2)
graph2.addEdge('C','F',5)
graph2.addEdge('C','E',9)
graph2.addEdge('D','C',2)
graph2.addEdge('D','E',7)
graph2.addEdge('E','D',7)
graph2.addEdge('E','C',9)
graph2.addEdge('E','F',1)
graph2.addEdge('F','C',5)
graph2.addEdge('F','E',1)
MST = kruskal(graph2.V, graph2.graph)
for i in MST:
    print(i)