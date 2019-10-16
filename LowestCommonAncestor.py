import collections

class Node:
    #constructor to create a new binary node
    def __init__(self,key,next_nodes):
        self.key = key
        self.parents = collections.deque(maxlen = 2)
        self.colour = None
        self.count = 0
        self.root = False

class lca:

    def find_lca(self, root, n1, n2):
        self.bfs(n1)
        self.bfs(n2)

        if root is None:
            return None
        if root.key == n1 or root.key == n2:
            return root
        left = self.find_lca(root.left, n1, n2)
        right = self.find_lca(root.right, n1, n2)

        if left and right:
            return root

        return left if left is not None else right

    def bfs(self,node):
        visited = []
        if node:
            visited.append(node) 
            print node.key
        current = node
        while current:
            if current.parents[0]
        
