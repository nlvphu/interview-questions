class Node:
    def __init__(self, identifier):
        self.id = identifier
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"Node({self.id})"
