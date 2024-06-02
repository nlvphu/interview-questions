import unittest
from graph import Graph

class TestGraphSearch(unittest.TestCase):

    def test_empty_graph(self):
        graph = Graph()
        self.assertFalse(graph.search('A', 'B'))

    def test_single_node(self):
        graph = Graph()
        graph.add_node('A')
        self.assertTrue(graph.search('A', 'A'))
        

    def test_connected_graph(self):
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'D')
        self.assertTrue(graph.search('A', 'D'))
        self.assertTrue(graph.search('A', 'C'))
        self.assertTrue(graph.search('B', 'D'))
        self.assertFalse(graph.search('D', 'A'))

    # def test_cycle_graph(self):
    #     graph = Graph()
    #     graph.add_edge('A', 'B')
    #     graph.add_edge('B', 'C')
    #     graph.add_edge('C', 'A')
    #     self.assertTrue(graph.search('A', 'C'))
    #     self.assertTrue(graph.search('B', 'A'))
    #     self.assertTrue(graph.search('C', 'B'))

    def test_self_loop(self):
        graph = Graph()
        graph.add_edge('A', 'A')
        self.assertTrue(graph.search('A', 'A'))

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

        self.assertTrue(graph.search('A', 'Z'))
        self.assertFalse(graph.search('Z', 'A'))
        self.assertTrue(graph.search('C', 'F'))
        self.assertFalse(graph.search('F', 'C'))
        self.assertTrue(graph.search('M', 'R'))
        self.assertFalse(graph.search('R', 'M'))

if __name__ == '__main__':
    unittest.main()