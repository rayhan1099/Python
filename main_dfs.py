from collections import defaultdict


def dfs(adjacent, visited, u):
    if u not in visited:
        visited.add(u)
        for element in adjacent[u]:
            if element not in visited:
                dfs(adjacent, visited, element)

    print(u, end=' ')


def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    adj = defaultdict(list)
    print("Enter edge info. One per line: ")

    for i in range(e):
        u, v = input("Enter edge %d: " % (i + 1)).split(' ')
        adj[u].append(v)
        # adj[v].append(u)

    print(adj)

    visitedO = set()
    print('DFS: ')
    for vertex in adj:
        if vertex not in visitedO:
            dfs(adj, visitedO, vertex)


if __name__ == "__main__":
    main()