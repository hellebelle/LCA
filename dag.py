from LowestCommonAncestor import Node

class DAG:

    def __init__(self, dag):
        self.dag = dag

    def add_node(self, key):
        for node, connections in self.dag.items():
            if key == node.key:
                return
        if key:
            self.dag[key] = []
        
    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)
        

    def add_edge(self,nodeA,node_list):
        if nodeA in self.dag:
            for i in node_list:
                if i in self.dag:
                    self.dag[nodeA].append(i)


    def find_path(self, nodeA, nodeB, path = []):
        path = path + [nodeA]
        if nodeA == nodeB:
            return path
        if not self.dag.has_key(nodeA):
            return None
    
        # visits all the nodes of a graph (connected component) using BFS
    def bfs(self, graph, start):
        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [start]
    
        # keep looping until there are nodes still to be checked
        while queue:
            # pop shallowest node (first node) from queue
            node = queue.pop(0)
            if node not in explored:
                # add node to list of checked nodes
                explored.append(node)
                neighbours = graph[node]
    
                # add neighbours of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored
if __name__ == "__main__":
    
    graph = {}
    dag = DAG(graph)

    dag.add_node(Node(1))
    
    # dag.add_edge(1,[4])
    # dag.add_edge(2,[4])
    # dag.add_edge(3,[4])
    # dag.add_edge(4,[5,6,7])
    # dag.add_edge(5,[8])
    # dag.add_edge(6,[8])
    # dag.add_edge(7,[8])
    '''dag.add_node(4)
    dag.add_node(6)
    dag.add_node(7)
    dag.add_node(8)

    dag.add_edge(4,[6,10])
    dag.add_edge(7,[4,6])
    '''
    #explored = dag.bfs(dag.dag, 1)

    for k, v in dag.dag.items():
        print(k.key)
    
    # print(explored)

