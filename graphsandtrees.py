class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.add_node(node1)
        if node2 not in self.adjacency_list:
            self.add_node(node2)

        #print(self.adjacency_list)
        
        
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def display_graph(self):
        for node in self.adjacency_list:
            print(f"{node}: {self.adjacency_list[node]}") 

mygraph = Graph()

nodeB = mygraph.add_node(node='B'), mygraph.add_edge('B', 'C'), mygraph.add_edge('B', 'D'), mygraph.add_edge('B', 'A')
nodeA = mygraph.add_node(node='A'), mygraph.add_edge('A', 'B'), mygraph.add_edge('A', 'D')
nodeC = mygraph.add_node(node='C'), mygraph.add_edge('C', 'B'), mygraph.add_edge('C', 'D')
nodeD = mygraph.add_node(node='D'), mygraph.add_edge('D', 'C'), mygraph.add_edge('D', 'A')
#print(f"Final Graph:\n\n{mygraph.adjacency_list}")


def depth_first_search_recursive(graph, current_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(current_node)
    
    print(current_node)
    
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            depth_first_search_recursive(graph, neighbor, visited)
graph = {
    'A' : ['B','C','D'],
    'B' : ['A', 'E', 'F'],
    'C' : [],
    'D' : ['A','G', 'H'],
    'E' : ['B'],
    'F' : ['B'],
    'G' : ['B'],
    'H' : ['B']
}


depth_first_search_recursive(graph, 'A')
