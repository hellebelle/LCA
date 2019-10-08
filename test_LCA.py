import unittest
from LowestCommonAncestor import Node
from LowestCommonAncestor import lca

class TestLCA(unittest.TestCase):

    def test_find_lca(self):
        lca_test = lca()

        root = Node(50)
        root.left = Node(15)
        root.right = Node(62)
        root.left.left = Node(5)
        root.left.right = Node(20)
        root.left.left.left = Node(3)
        root.left.left.right = Node(8)
        root.left.right.right = Node(37)
        root.left.right.right.left = Node(24)
        root.right.left = Node(58)
        root.right.left.right = Node(60)
        root.right.right = Node(91)


        self.assertEqual(lca_test.find_lca(root, root.left.left.right, root.left.left ), 15)



if __name__ == '__main__':
    unittest.main()