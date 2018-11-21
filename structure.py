class Node:
    __id = 0
    def __init__(self, name):
        self.id = Node.__id
        self.name = name
        Node.__id += 1

class Graph:
    """ Our class for creating the data structure """
    def __init__(self):
        self._graph = {}
    def add(self, node):
        if not self.nodeExists(node):
            self._graph[node] = []
            print("%s has been registered"%node.name)
        else:
            print("object was already here")
    def nodeExists(self, node):
        for element in self._graph:
            if element == node:
                return True
        return False
    def getNode(self,id):
        for element in self._graph:
            if element.id == int(id):
                return element
        return False
    def getNodes(self):
        response = []
        for element in self._graph:
            response.append(element)
        return response 
    def connect(self, node1, node2):
        if self.nodeExists(node1) and self.nodeExists(node2):
            self._graph[node1].append(node2)
            self._graph[node2].append(node1)
            print("connection between %s and %s was made"%(node1.name,node2.name))
        else:
            print("one node doesnt exist")
    def print_raw(self):
        print (self._graph)
    def print(self):
        for element in self._graph:
            print("%s has the following connections"%element.name)
            for connections in self._graph[element]:
                print("\t%s"%connections.name)
    def connections(self, node):
        return self._graph[node]