#   [A] -------- [B]
#    |   \
#    |     \   
#    |        \
#   [C] -------- [D]
#   
#      A  B  C  D
#   A  0  1  1  1
#   B  1  0  0  0
#   C  1  0  0  1
#   D  1  0  1  0

nodes = ['A', 'B', 'C', 'D']
graph2 = [
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
]

class node:
    def __init__(self, name, size):
        self.name = name
        self.edges = [None] * size
    def connect(self, node_name):
        for x in range(len(self.edges)):
            if self.edges[x] == node_name:
                break
            if self.edges[x] == None:
                self.edges[x] = node_name
                break
    def display(self):
        print(self.name)
        print(self.edges)

class graph:
    def __init__(self, size):
        self.nodes = [None] * size
        self.size = size
    def display(self):
        for x in range(len(self.nodes)):
            if (self.nodes[x] != None):
                print(self.nodes[x].name)
                print(self.nodes[x].edges)
    def create_node(self, node_name):
        new_node = node(node_name, self.size - 1)
        for x in range(len(self.nodes)):
            if self.nodes[x] == new_node:
                break
            if self.nodes[x] == None:
                self.nodes[x] = new_node
                break
    def create_connection(self, origin, destination):
        for x in range(len(self.nodes)):
            if self.nodes[x] != None:
                if self.nodes[x].name == origin:
                    self.nodes[x].connect(destination)
                if self.nodes[x].name == destination:
                    self.nodes[x].connect(origin)

G = graph(10)
G.create_node('A')
G.create_node('B')
G.create_node('C')
G.create_node('D')
G.create_connection('A', 'B')
G.create_connection('A', 'C')
G.create_connection('A', 'D')
G.create_connection('C', 'D')
G.display()

#a = node('A')
#a.connect('B')
#a.connect('C')
#a.connect('C')
#a.display()