from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, identifier):
        if identifier not in self.nodes:
            self.nodes[identifier] = Node(identifier)

    def add_edge(self, u, v):
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)
        self.nodes[u].add_neighbor(self.nodes[v])
    
    def get_adj_list(self):
        adj_list = {}
        for node in self.nodes.values():
            adj_list[node.id] = [neighbor.id for neighbor in node.neighbors]
        return adj_list

    def search(self, start, target):

        
        
        pass  # Replace with your search algorithm