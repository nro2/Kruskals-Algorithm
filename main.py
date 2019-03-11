from BuildGraph import Graph
from BuildGraph import readinFile
from collections import defaultdict

vertices = []

def find(vertex, keys):
    for i in range(len(keys)):
        if vertex == keys[i]:
            print("inside if")
            return i


def union(vertex1, vertex2, keys):
    print("inside union")
    index1 = find(vertex1, keys)
    index2 = find(vertex2, keys)
    for element in keys[index2]:
        keys[index1].append(element)
    keys.pop(index2)


def kruskal(V, G):


    MST = []
    keys = list(G.keys())
    edges = []

    weight = 0

    for i in range(0, len(keys)):
        for j in range(0, len(G[keys[i]])):
            edges.append([keys[i], G[keys[i]][j][0], G[keys[i]][j][1]])  #Pull everything from dictionary and put into an array

    edges = sorted(edges, key=lambda item: int(item[2]))                        #Sort edges array by weight

  #  for i in range(len(edges)):                                             #Make sets of all edges
  #      if edges[i][0] not in vertices:
  #          vertices.append(edges[i][0])

    while len(MST) != V - 1:
        print("Inside while")
        for e in range(0, len(edges)):
            if find(edges[e][0], keys)!= find(edges[e][1], keys):
                print("inside while if")
                union(edges[e][0], edges[e][1], keys)
                weight += edges[e][2]
                MST.append(edges[e])
    print("outside while")
    print("Total Weight: ", weight)
    return MST



myGraph = Graph()
readinFile(myGraph, "city-pairs.txt")
MST = kruskal(myGraph.V, myGraph.graph)
for i in MST:
    print(i)