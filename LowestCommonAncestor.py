class Node:
    #constructor to create a new binary node
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def find_lca(root, n1, n2):
    if root is None:
        return None
    if root.key == n1 or root.key == n2:
        return root
    left = find_lca(root.left, n1, n2)
    right = find_lca(root.right, n1, n2)

    if left and right:
        return root

    return left if left is not None else right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4,5) = ", find_lca(root, 4, 5).key)
print("LCA(4,6) = ", find_lca(root, 4, 6).key)
print("LCA(3,4) = ", find_lca(root, 3, 4).key)
print("LCA(2,4) = ", find_lca(root, 2, 4).key)