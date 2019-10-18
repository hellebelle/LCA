import networkx

class lca:

    def do_lca(self, graph, x, y):
        lca = networkx.algorithms.lowest_common_ancestor(graph, x, y)
        return lca

    def check_acyclic(self, graph):
        if_acyclic = networkx.is_directed_acyclic_graph(graph)
        return if_acyclic

# if __name__ == "__main__":
#     lca = lca()

#     G = networkx.DiGraph()
#     map(G.add_node, range(1, 8))
#     G.add_edge(1, 2)
#     G.add_edge(1, 3)
#     G.add_edge(2, 4)
#     G.add_edge(2, 5)
#     G.add_edge(3, 6)
#     G.add_edge(4, 7)
#     G.add_edge(5, 7)
#     G.add_edge(6, 5)
#     G.add_edge(6, 7)

#     lca_a = lca.do_lca(G, 4, 6)
#     if_acyclic = lca.check_acyclic(G)
#     print(if_acyclic)
#     print(lca_a)




    	
