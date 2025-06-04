class Graphtest:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict() #This extension is a data dictionary
        self.adj_matrix = None

        """
        
        graph = {
            A:(B,2), (C,3), (D,1)
            B:(E,2), (F,3), (G,1)
            Z:(L,2), (G,3), (W,1)
        }
        
        """


    def __repr__(self):
        graph_string=""

        for node, neighbors in self.adj_list.items():
            graph_string += f"{node} -> {neighbors}\n"

        return graph_string

    def bfs(self, starting_node):
        visited = set()

        queue = [starting_node]
        order = []

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                order.append(node)
                
                neighbours = self.obtain_neighbours(node)

                for neighbour in neighbours:
                   if isinstance(neighbour, tuple): #This just extracts the weight only
                       neighbour = neighbour[0]

                   if neighbour not in visited:
                       queue.append(neighbour)

        return order


    def dfs(self, starting_node):
        visited = set()

        stack = [starting_node]
        order = []

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                order.append(node)

                neighbours = self.obtain_neighbours(node)

                for neighbour in sorted(neighbours, reverse=True):
                    if isinstance(neighbour, tuple):  # This just extracts the weight only
                        neighbour = neighbour[0]


                    if neighbour not in visited:
                        stack.append(neighbour)

        return order




    def add_node(self, data): # Adding a key to the dictionary
        if data in self.adj_list.keys():
            raise ValueError("Node already exists")
        else:
            self.adj_list[data] = set()

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list.keys():
            self.adj_list[from_node] = set()

        if to_node not in self.adj_list.keys():
            self.adj_list[to_node] = set()

        if weight is not None:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

        else:
            self.adj_list[from_node].add(to_node)
            if not self.directed: #Check if directed or not directed
                self.adj_list[to_node].add(from_node)

    def obtain_neighbours(self, node):
        return self.adj_list.get(node, set())




if __name__ == "__main__":
    test = Graphtest(directed=True)

    test.add_edge("A", "B", 2)
    test.add_edge("A", "J", 1)
    test.add_edge("A", "C", 3)
    test.add_edge("A", "D", 4)
    test.add_edge("C", "D", 7)
    test.add_edge("B", "D", 5)


    print(test.__repr__())



    print("Breadth First Search")
    print(test.bfs("B"))


    print("Depth-First Search")
    print(test.dfs("D"))
