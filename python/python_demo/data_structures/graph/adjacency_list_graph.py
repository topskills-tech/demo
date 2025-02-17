class Graph:
    """Graph represented using an adjacency list"""
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        """Add an edge between vertex u and vertex v"""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph

    def display(self):
        """Display the adjacency list"""
        for vertex, edges in self.adj_list.items():
            print(vertex, "->", edges)

    def bfs(self, start):
        """Breadth-First Search traversal"""
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(set(self.adj_list[vertex]) - visited)
        print()

    def dfs(self, start, visited=set()):
        """Depth-First Search traversal"""
        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor in self.adj_list[start]:
                self.dfs(neighbor, visited)

def demo_graph():
    print("=================================================")
    print("Demo of graph implementation using adjacency list")
    print("=================================================")
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.display()
    print("BFS Traversal:")
    graph.bfs(1)
    print("DFS Traversal:")
    graph.dfs(1)