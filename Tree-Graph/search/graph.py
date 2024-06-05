from node import Node
import queue
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
    

    def dfs(self, start, end, visited):
        visited = []
        return self.dfs_search(start, end, visited)

    
    def dfs_search(self, start, end, visited):
        if start == end:
            return True
        
        visited.append(start)
        
        for neighbor in self.nodes[start].neighbors:
            if neighbor not in visited:
                return self.dfs_search(neighbor.id, end, visited)

        return False
    
    def bfs(self, start, end):
        if start == end:
            return True

        visited = []
        q = queue.Queue()

        visited.append(start)
        q.put(start)

        while not q.empty():
            node = q.get()
            visited.append(node)
            
            if node == end:
                return True
        
            for neighbor in self.nodes[node].neighbors:
                if neighbor not in visited:
                    q.put(neighbor.id)
        
        return False