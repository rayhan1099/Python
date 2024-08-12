from collections import defaultdict


def dfs(adj,visited, vertex):
    if vertex not in visited:
        visited.add(vertex)

        for element in adj[vertex]:
            if element not in visited:
                dfs(adj,visited,element)
    print(vertex, end=' ')


n = int(input("Enter Number of Nodes: "))
e = int(input("Enter Number of Edges: "))

adj = defaultdict(list)

for i in range(e):
    vertex, edge = input("Edge %d: " % (i+1)).split()
    adj[vertex].append(edge)

print(adj)
t = []
visited = set()

for vertex in list(adj):
    if vertex not in visited:
        dfs(adj, visited,vertex)