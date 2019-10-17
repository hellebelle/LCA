from pprint import pprint

class DAG:

    def __init__(self, dag):
        self.dag = dag

    def add_node(self, key):
        for k, v in self.dag.items():
            if key == k:
                return
        if key:
            self.dag[key] = []
        

    def add_edge(self,nodeA,node_list):
        if nodeA in self.dag:
            for i in node_list:
                if i in self.dag:
                    self.dag[nodeA].append(i)


    def find_path(self, nodeA, nodeB):
        pass

if __name__ == "__main__":
    graph = {}
    dag = DAG(graph)

    dag.add_node(4)
    dag.add_node(6)
    dag.add_node(7)
    dag.add_node(10)

    dag.add_edge(4,[6,10])
    dag.add_edge(7,[4,6])
    for k, v in dag.dag.items():
        print(k,v)
    

