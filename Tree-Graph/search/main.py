import unittest
from graph import *

class TestGraphSearch(unittest.TestCase):

    # def test_empty_graph(self):
    #     graph = Graph()
    #     self.assertFalse(graph.dfs('A', 'B', False))

    # def test_single_node(self):
    #     graph = Graph()
    #     graph.add_node('A')
    #     self.assertTrue(graph.dfs('A', 'A', False))
        

    def test_connected_graph(self):
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'D')
        self.assertTrue(graph.dfs('A', 'D', False))
        self.assertTrue(graph.dfs('A', 'C', False))
        self.assertTrue(graph.dfs('B', 'D', False))
        self.assertFalse(graph.dfs('D', 'A', False))

        self.assertTrue(graph.bfs('A', 'D'))
        self.assertTrue(graph.bfs('A', 'C'))
        self.assertTrue(graph.bfs('B', 'D'))
        self.assertFalse(graph.bfs('D', 'A'))


    def test_complex_graph(self):
        graph = Graph()
        edges = [
            ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), 
            ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'),
            ('J', 'K'), ('K', 'L'), ('L', 'M'), ('M', 'N'), ('N', 'O'),
            ('O', 'P'), ('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'T'),
            ('T', 'U'), ('U', 'V'), ('V', 'W'), ('W', 'X'), ('X', 'Y'),
            ('Y', 'Z')
        ]
        for u, v in edges:
            graph.add_edge(u, v)

        self.assertTrue(graph.dfs('A', 'Z', False))
        self.assertFalse(graph.dfs('Z', 'A', False))
        self.assertTrue(graph.dfs('C', 'F', False))
        self.assertFalse(graph.dfs('F', 'C', False))
        self.assertTrue(graph.dfs('M', 'R', False))
        self.assertFalse(graph.dfs('R', 'M', False))

        self.assertTrue(graph.bfs('A', 'Z'))
        self.assertFalse(graph.bfs('Z', 'A'))
        self.assertTrue(graph.bfs('C', 'F'))
        self.assertFalse(graph.bfs('F', 'C'))
        self.assertTrue(graph.bfs('M', 'R'))
        self.assertFalse(graph.bfs('R', 'M'))

if __name__ == '__main__':
    unittest.main()