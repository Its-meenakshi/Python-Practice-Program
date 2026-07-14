def movgen(node, graph):
    return graph[node]

def a_star(graph, heuristic, start, goal):
    OPEN = [start]
    CLOSED = []
    parent = {start: None}
    g = {start: 0}
    f = {start: heuristic[start]}

    while OPEN:
        current = min(OPEN, key=lambda x: f[x])
        OPEN.remove(current)

        print("Expanding Node:", current)
        print("g(n):", g[current], "f(n):", f[current])

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Final Path:", path)
            print("Total Cost:", g[goal])
            return

        for child, cost in movgen(current, graph):
            new_cost = g[current] + cost

            if child not in g or new_cost < g[child]:
                parent[child] = current
                g[child] = new_cost
                f[child] = new_cost + heuristic[child]

                if child in CLOSED:
                    CLOSED.remove(child)
                if child not in OPEN:
                    OPEN.append(child)

        CLOSED.append(current)
        print("OPEN List:", OPEN)
        print("CLOSED List:", CLOSED)
        print("-" * 50)

    print("Goal not found")


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 7,
    'E': 2,
    'F': 6,
    'G': 0
}

a_star(graph, heuristic, 'A', 'G')