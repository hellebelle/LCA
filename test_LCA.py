import unittest
from LowestCommonAncestor import Node
from LowestCommonAncestor import lca

class TestLCA(unittest.TestCase):

    def test_find_lca(self):
        self.assertEqual(lca.find_lca(fdfd), 1)



if __name__ == '__main__':
    unittest.main()