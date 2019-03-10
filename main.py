from BuildGraph import Graph
from BuildGraph import readinFile
from collections import defaultdict

vertices = []

def find(vertex):
    for i in range(len(vertices)):
        for element in vertices[i]:
            if element == vertex:
                return i
    return None

def union(vertex1, vertex2):
    index1 = find(vertex1)
    index2 = find(vertex2)
    for element in vertices[index2]:
        vertices[index1].append(element)
    vertices.pop(index2)


def kruskal(V, G):

    MST = []
    keys = list(G.keys())
    edges = []

    weight = 0

    for i in range(0, len(keys)):
        for j in range(0, len(G[keys[i]])):
            edges.append([keys[i], G[keys[i]][j][0], G[keys[i]][j][1]])  #Pull everything from dictionary and put into an array

    edges = sorted(edges, key=lambda item: item[2])                        #Sort edges array by weight

    for i in range(len(edges)):                                             #Make sets of all edges
            for j in range(len(edges[i])):
                if edges[i][j] not in vertices:
                    vertices.append(edges[i][j])

    while len(MST) != V - 1:

        for e in range(0, len(edges)):
            if find(edges[i][0]) != find(edges[i][1]):
                union(edges[i][0], edges[i][1])
                weight += edges[i][2]
                MST.append(edges[i])

    print("Total Weight: ", weight)
    return MST



myGraph = Graph()
readinFile(myGraph, "city-pairs.txt")
MST = kruskal(myGraph.V, myGraph.graph)
for i in MST:
    print(i)