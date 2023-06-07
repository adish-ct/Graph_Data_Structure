class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            print("The node is already present")
        else:
            self.adjacency_list[vertex] = []

    def add_edges(self, node, edge):
        if edge not in self.adjacency_list:
            print("neighbour is not found")
            return
        if node not in self.adjacency_list:
            self.adjacency_list[node] = [edge]
        else:
            if edge in self.adjacency_list[node]:
                print("edge is existing")
                return
            else:
                self.adjacency_list[node].append(edge)
                self.adjacency_list[edge].append(node)

    def delete(self, node):
        del self.adjacency_list[node]
        for i in self.adjacency_list:
            values = self.adjacency_list[i]
            if node in values:
                values.remove(node)

    # graph traversing DFS

    def dfs(self, node):
        if node not in self.adjacency_list:
            print("node is not present")
            return
        visited = set()
        stack = []
        stack.append(node)
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current, end=", ")
                visited.add(current)
                for i in self.adjacency_list[current]:
                    stack.append(i)
        return visited

    def check(self, v1, v2):

        if v1 and v2 in self.adjacency_list:
            values_in_1 = self.adjacency_list[v1]
            values_in_2 = self.adjacency_list[v2]
            if v1 in values_in_2:
                print("its connected")
            else:
                print("its not connected")
            if v2 in values_in_1:
                print("its connected")
            else:
                print("its not connected")
        else:
            print("vertices is not present in the list")


    def display(self):
        print(self.adjacency_list)






g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_edges(1, 2)
g.add_edges(2, 4)
g.add_edges(3, 5)
g.add_edges(5, 4)
g.add_edges(4, 1)
g.add_edges(2, 5)
g.add_edges(2, 0)

print("traverse :", g.dfs(2))

print(g.display())

g.check(1, 5)
