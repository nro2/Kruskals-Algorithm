from collections import defaultdict


class Graph():
    def __init__(self):
        self.verticies = set()
        self.V = 0
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):

        if src not in self.verticies:
            self.verticies.add(src)
            self.V += 1

        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)


def readinFile(aGraph, file):
    with open(file) as f:
        for line in f:
            linedata = line.split(' ')
            aGraph.addEdge(linedata[0], linedata[1], linedata[2].rstrip('\n'))