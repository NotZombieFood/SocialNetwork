class Node:
    """
        Description: Node class, every user will be one
        Data:
            id: unique id for every user
            name: just the name of the users
    """
    __id = 0
    def __init__(self, name):
        self.id = Node.__id
        self.name = name
        Node.__id += 1

class Graph:
    """ Description: Our class for creating the data structure
        Methods: add, getNode, getNodes, connect, print, connections
        Init: Doesnt require anything 
        TODO: Connect request  Connect Confirmation 
    """
    def __init__(self):
        self._graph = {}
    def add(self, node):
        """
            Description: Adds node to the graph, but doesnt connect anything... example a new user with no friends
            Params: A Node object
            Return: None
        """
        if not self._nodeExists(node):
            self._graph[node] = []
            print("%s has been registered"%node.name)
        else:
            print("object was already here")
    def _nodeExists(self, node):
        """
            Description: Private method for checking if node exists
        """
        for element in self._graph:
            if element == node:
                return True
        return False
    def getNode(self,id):
        """
            Description: Get the node object which has the id received
            Params: id as a string (the way flask is sending it)
            Return: False if not found and the object if found
        """
        for element in self._graph:
            if element.id == int(id):
                return element
        return False
    def getNodes(self):
        """
            Description: Get all nodes objects
            Return: All nodes
        """
        response = []
        for element in self._graph:
            response.append(element)
        return response 
    def connect(self, node1, node2):
        """
            Description: Connect two nodes
            Params: Both nodes objects
            Return: None
            TODO: Define if this will be a private method, it should be as I see it 
        """
        if self._nodeExists(node1) and self._nodeExists(node2):
            self._graph[node1].append(node2)
            self._graph[node2].append(node1)
            print("connection between %s and %s was made"%(node1.name,node2.name))
        else:
            print("one node doesnt exist")
    def print(self):
        """
            Description: Print all the graph in a readable way, may add it as a debug webpage or something (can we do a tree??)
            Return: None
        """
        for element in self._graph:
            print("%s has the following connections"%element.name)
            for connections in self._graph[element]:
                print("\t%s"%connections.name)
    def dictionary(self):
        """
            Description: Gives back de full dictionary we have created
            Return: A dict
        """
        return self._graph
    def connections(self, node):
        """ 
            Description: Gives back the connections from a user
            Params: a Node object
            Return: Array of node objects which the user has connected with
        """
        return self._graph[node]