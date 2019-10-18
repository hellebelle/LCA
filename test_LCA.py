import unittest
import networkx
from LowestCommonAncestor import lca

class TestLCA(unittest.TestCase):

    def test_find_lca(self):
        lca_test = lca()

        G = networkx.DiGraph()
        map(G.add_node, range(1, 8))
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(2, 5)
        G.add_edge(3, 6)
        G.add_edge(4, 7)
        G.add_edge(5, 7)
        G.add_edge(6, 5)
        G.add_edge(6, 7)
         
        self.assertEqual(lca_test.do_lca(G, 4, 6), 1)

    def test_check_acyclic(self):
        lca_test = lca()

        G = networkx.DiGraph()
        map(G.add_node, range(1, 8))
        G.add_edge(1, 2)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        G.add_edge(2, 5)
        G.add_edge(3, 6)
        G.add_edge(4, 7)
        G.add_edge(5, 7)
        G.add_edge(6, 5)
        G.add_edge(6, 7)
         
        self.assertEqual(lca_test.check_acyclic(G), True)

if __name__ == '__main__':
    unittest.main()