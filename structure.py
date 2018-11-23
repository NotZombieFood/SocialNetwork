import random, collections
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
        self._pendingRequests = {}
        self._sentRequests = {}
    def _nodeExists(self, node):
        """
            Description: Private method for checking if node exists
        """
        for element in self._graph:
            if element == node:
                return True
        return False
    def delete(self, node):
        """
            Description: delete node from the graph, clear connections
            Params: A Node object
            Return: None
        """
        if  self._nodeExists(node):
            del self._graph[node]
            del self._pendingRequests[node]
            del self._sentRequests[node]
            for element in self._graph:
                for subelement in self._graph[element]:
                    if subelement == node:
                        self._graph[element].remove(node)
            for element in self._pendingRequests:
                for subelement in self._pendingRequests[element]:
                    if subelement == node:
                        self._pendingRequests[element].remove(node)
            for element in self._sentRequests:
                for subelement in self._sentRequests[element]:
                    if subelement == node:
                        self._sentRequests[element].remove(node)
            print("%s has been deleted"%node.name)
        else:
            print("object was not here")
    def add(self, node):
        """
            Description: Adds node to the graph, but doesnt connect anything... example a new user with no friends
            Params: A Node object
            Return: None
        """
        if not self._nodeExists(node):
            self._graph[node] = []
            self._pendingRequests[node] = []
            self._sentRequests[node] = []
            print("%s has been registered"%node.name)
        else:
            print("object was already here")
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
    def getByName(self,name):
        """
            Description: Get the node object which has the name received
            Params: name as a string (the way flask is sending it)
            Return: False if not found and the object if found
        """
        for element in self._graph:
            if element.name == name:
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
    def sendRequest(self, sender_node, recipient_node):
        """
            Description: send a friend request, writes both dicts
            Params: Both nodes objects
            Return: None
        """
        if sender_node != recipient_node and self._nodeExists(sender_node) and self._nodeExists(recipient_node) and recipient_node not in self._sentRequests[sender_node] and sender_node not in self._pendingRequests[recipient_node] and sender_node not in self._graph[recipient_node]:
            self._pendingRequests[recipient_node].append(sender_node)
            self._sentRequests[sender_node].append(recipient_node)
            return True
        else:
            print("one node doesnt exist or have been send before")
            return False
    def acceptRequest(self, sender_node, recipient_node):
        """
            Description: send a friend request, writes both dicts
            Params: Both nodes objects
            Return: None
        """
        if self._nodeExists(sender_node) and self._nodeExists(recipient_node) and recipient_node in self._sentRequests[sender_node] and sender_node in self._pendingRequests[recipient_node]:
            self._pendingRequests[recipient_node].remove(sender_node)
            self._sentRequests[sender_node].remove(recipient_node)
            self.connect(sender_node,recipient_node)
        else:
            print("one node doesnt exist or have not been sent")
    def friendReceivedRequests(self, node):
        """ 
            Description: Gives back the friend request for a user
            Params: a Node object
            Return: Array of node objects which the user has connected with
        """
        return self._pendingRequests[node]
    def friendSentRequests(self, node):
        """ 
            Description: Gives back the friend sent for a user
            Params: a Node object
            Return: Array of node objects which the user has connected with
        """
        return self._sentRequests[node]
    def connect(self, node1, node2):
        """
            Description: Connect two nodes
            Params: Both nodes objects
            Return: None
            TODO: Define if this will be a private method, it should be as I see it 
        """
        if node1 != node2 and self._nodeExists(node1) and self._nodeExists(node2) and node2 not in self._graph[node1] and node1 not in self._graph[node2]:
            self._graph[node1].append(node2)
            self._graph[node2].append(node1)
            print("connection between %s and %s was made"%(node1.name,node2.name))
        else:
            print("one node doesnt exist or connection already exists")
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
    def randomConnections(self):
        usuarios = len(self._graph)
        for element in self._graph:
            friendCount = random.randint(1,usuarios-1)
            for i in range(friendCount-1):
                id = random.randint(0,usuarios-1)
                self.connect(element,self.getNode(id))
    def randomRequests(self):
        usuarios = len(self._graph)
        for element in self._graph:
            friendCount = random.randint(1,usuarios-1)
            for i in range(friendCount-1):
                id = random.randint(0,usuarios-1)
                self.sendRequest(element,self.getNode(id))
    def linearSearch(self, node, name):
        for element in self.getNodes():
            if name == element.name:
                return element
        return None #returned when the name is not found
    def obtainSet(self):
        dictionary = {}
        for element in self._graph:
            array = []
            for subelement in self._graph[element]:
                array.append(subelement.name)
            dictionary[element.name] = set(array)
        return dictionary
    def bfs_path(self, start, goal):
        """ Heavily inspired by:    
            https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
        """
        set_graph = self.obtainSet()
        queue = [(start, [start])] #the queue begins with the name of the user
        while queue:
            (vertex, path) = queue.pop(0) #let the vertex be the last one search in and path be the where we have been
            for next in set_graph[vertex] - set(path): #dont count the old path
                if next == goal: #we find our goal
                    return path + [next]
                else:
                    queue.append((next, path + [next])) #the one we seached is on the queue, plus an array with the previous visits and the last one
