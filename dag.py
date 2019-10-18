# from LowestCommonAncestor import Node

# class DAG:

#     def __init__(self, dag):
#         self.dag = dag

#     def add_node(self, node):
#         for n, connections in self.dag.items():
#             if n.key == node.key:
#                 return
#         if node:
#             self.dag[node] = []
        
#     def add_nodes(self, nodes):
#         for n in nodes:
#             node = Node(n)
#             self.add_node(node)
        

#     def add_edge(self,nodeA,node_list):
#         for i in self.dag.keys():
#             if nodeA.key == i.key:
#                 for j in node_list:
#                     self.dag[i].append(j)
                    


#     # def find_path(self, nodeA, nodeB, path = []):
#     #     path = path + [nodeA]
#     #     if nodeA == nodeB:
#     #         return path
#     #     if not self.dag.has_key(nodeA):
#     #         return None
    
#         # visits all the nodes of a graph (connected component) using BFS
#     def bfs(self, start):
#         # keep track of all visited nodes
#         explored = []
#         # keep track of nodes to be checked
#         queue = [start]
    
#         # keep looping until there are nodes still to be checked
#         while queue:
#             # pop shallowest node (first node) from queue
#             node = queue.pop(0)
#             if node not in explored:
#                 # add node to list of checked nodes
#                 explored.append(node)
#                 neighbours = self.dag[Node(node)]
    
#                 # add neighbours of node to queue
#                 for neighbour in neighbours:
#                     queue.append(Node(neighbour))
#         return explored

#     def print_graph(self, graph):
#         g = {}
#         for k, v in graph.items():
#             edges = []
#             for i in v:
#                 edges.append(i.key)
#             g[k.key] = edges

#         for k, v in g.items():
#             print(k, v)

# if __name__ == "__main__":
    
#     graph = {}
#     dag = DAG(graph)
#     nodes = list(range(1,9))
#     dag.add_nodes(nodes)
    
#     dag.add_edge(Node(1),[Node(4)])
#     dag.add_edge(Node(2),[Node(4)])
#     dag.add_edge(Node(3),[Node(4)])
#     dag.add_edge(Node(4),[Node(5),Node(6),Node(7)])
#     dag.add_edge(Node(5),[Node(8)])
#     dag.add_edge(Node(6),[Node(8)])
#     dag.add_edge(Node(7),[Node(8)])

#     #explored = dag.bfs(1)
#     #dag.print_graph(dag.dag)
#     node = Node(1)
#     for j in dag.dag.keys:
#         if node.key == j.key:
#             result = 
#     print(result)
    
#     #print(explored)

